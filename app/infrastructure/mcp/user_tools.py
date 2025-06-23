from fastmcp import FastMCP
from app.config.settings import get_settings
from app.interfaces.mcp.tools_handlers import IToolsController
import json
from textblob import TextBlob
from starlette.responses import PlainTextResponse

settings = get_settings()

class MCPToolsController(IToolsController):

    _mcp = FastMCP(name=settings.NAME, instructions="Your instructions here")

    stream = "streamable-http"
    sse = "sse"
    _mcp_app = _mcp.http_app(path="/v1", transport="sse")
    """
    This class is a placeholder for MCP tools controller.
    You can implement methods to handle MCP requests here.
    """
    def sentiment_analysis(self, text: str) -> str:
        """
        Analyze the sentiment of the given text.

        Args:
            text (str): The text to analyze

        Returns:
            str: A JSON string containing polarity, subjectivity, and assessment
        """
        blob = TextBlob(text)
        sentiment = blob.sentiment
        
        result = {
            "polarity": round(sentiment.polarity, 2),  # -1 (negative) to 1 (positive) # type: ignore
            "subjectivity": round(sentiment.subjectivity, 2),  # 0 (objective) to 1 (subjective) #type: ignore
            "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral" # type: ignore
        }

        return json.dumps(result)
    def health_check(self) -> PlainTextResponse:
        """
        Perform a health check of the MCP tools.

        Returns:
            str: A simple health check message
        """
        return PlainTextResponse("OK", status_code=200)
    
    #create a static method to instantiate the controller and registers the tools
