# main.py (or wherever you bootstrap your server)
# Wire up the application with FastAPI, SQLAlchemy, and MCP

from fastapi import FastAPI
from sqlalchemy import create_engine
from app.infrastructure.api.user_routes import UserRouter
from app.infrastructure.api.static_routes import app as static_routes
from app.infrastructure.persistence.user_repo import UserRepository
from app.infrastructure.mcp.user_tools import MCPToolsController as mcp_controller
from app.config.logging_config import setup_logging
from app.config.settings import get_settings
import pyodbc 

# load settings, logging, etc.
settings = get_settings()
setup_logging()

# 1. Create a real FastAPI app (not APIRouter)
app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=mcp_controller._mcp_sse_app.lifespan,
)

# 2. Wire up your DB
engine = create_engine(settings.DATABASE_URL)
user_repository = UserRepository(engine=engine)

# 3. Register your domain routers
user_router = UserRouter(user_repository=user_repository)
user_router.register_routes()
app.include_router(user_router._app, prefix="/api/v1", tags=["users"])
app.include_router(static_routes, tags=["static"])
# (Optional) serve SPA / static routes under their own prefix:
# app.mount("/", StaticFiles(directory="path/to/dist", html=True), name="spa")

# mount my MCP app
mcp_router = mcp_controller()

mcp_router._mcp.tool(mcp_router.sentiment_analysis)
app.mount("/mcp/sse", mcp_router._mcp_sse_app, name="mcp") # mcp endpoint path /mcp/v1


# 4. Check your drivers early
odbc_drivers = pyodbc.drivers()
if not odbc_drivers:
    raise RuntimeError("No ODBC drivers found. Please install the ODBC Driver for SQL Server.")
