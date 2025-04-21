# main.py
from fastmcp import FastMCP
import os
import json
import httpx
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
BRAVE_API_KEY  = os.getenv("BRAVE_API_KEY")


# Create your MCP server instance
mcp = FastMCP("Multi-Search")

# --- Google Search via SerpApi ---
@mcp.tool()
async def google_search(query: str) -> str:
    """Run a Google search via SerpApi (no CX needed)."""
    if not GOOGLE_API_KEY:
        raise RuntimeError("GOOGLE_API_KEY must be set")
    search = GoogleSearch({"q": query, "api_key": GOOGLE_API_KEY})
    result = search.get_dict()
    return json.dumps(result)

# --- Brave News Search ---
@mcp.tool()
async def brave_search(query: str) -> str:
    """Fetch search results from Brave News API."""
    if not BRAVE_API_KEY:
        raise RuntimeError("BRAVE_API_KEY must be set")
    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    params = {"q": query, "count": 10, "freshness": "week"}
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://api.search.brave.com/res/v1/news/search",
            headers=headers,
            params=params
        )
        return r.text

# --- DuckDuckGo Instant Answer ---
@mcp.tool()
async def duck_search(query: str) -> str:
    """Query DuckDuckGo Instant Answer API (no key required)."""
    params = {"q": query, "format": "json", "no_html": 1, "skip_disambig": 1}
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.duckduckgo.com/", params=params)
        return resp.text

# …include any existing weather & notes tools here…

# Entry point: start the MCP server over stdio
if __name__ == "__main__":
    mcp.run()
