from fastmcp import FastMCP
import os
import json
import httpx
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Load any .env overrides locally
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")    # optional now
BRAVE_API_KEY  = os.getenv("BRAVE_API_KEY")     # still required

mcp = FastMCP("Multi-Search")

@mcp.tool()
async def google_search(query: str) -> str:
    """Run a Google search via SerpApi (Custom Search no longer needed)."""
    if not GOOGLE_API_KEY:
        raise RuntimeError("GOOGLE_API_KEY is not set")
    search = GoogleSearch({"q": query, "api_key": GOOGLE_API_KEY})
    return json.dumps(search.get_dict())

@mcp.tool()
async def brave_search(query: str) -> str:
    """Fetch search results from Brave News API."""
    if not BRAVE_API_KEY:
        raise RuntimeError("BRAVE_API_KEY is not set")
    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    params = {"q": query, "count": 10, "freshness": "week"}
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://api.search.brave.com/res/v1/news/search",
            headers=headers,
            params=params
        )
        return resp.text

@mcp.tool()
async def duck_search(query: str) -> str:
    """Query DuckDuckGo Instant Answer API (no key required)."""
    params = {"q": query, "format": "json", "no_html": 1, "skip_disambig": 1}
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.duckduckgo.com/", params=params)
        return resp.text

if __name__ == "__main__":
    mcp.run()
