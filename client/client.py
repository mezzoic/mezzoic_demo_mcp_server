import asyncio
from fastmcp import Client

config = {
    "mcpServers": {
        # A remote HTTP server
        "test":{
            "url": "http://localhost:8000/mcp/sse/v1/",
            "transport": "sse"
        }
    }
}


client = Client(config)

async def main():
    async with client:
        print(f"Client connected {client.is_connected()}, transport url: {client.transport.transport.url}, using transport type: {client.transport.transport}") # type: ignore

        tools = await client.list_tools()
        print("Available tools:", tools)

        if any( tool.name == "sentiment_analysis" for tool in tools):
            result = await client.call_tool("sentiment_analysis", { "text":"I love programming with FastMCP!"})
            print("Sentiment Analysis Result:", result)

if __name__ == "__main__":
    asyncio.run(main())