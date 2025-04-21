[![smithery badge](https://smithery.ai/badge/@sanjoy1234/multi-search-mcp)](https://smithery.ai/server/@sanjoy1234/multi-search-mcp)

# Multi‑Search MCP Server

A lightweight MCP server that **unifies multiple search engines** under one simple stdio API. Query Google, Brave News, and DuckDuckGo—without juggling three different SDKs or payload formats.

---

## 🔍 What It Does

- **Google Search** via SerpApi (JSON‑first, optional key)
- **Brave News** retrieval through Brave’s News API (key required)
- **DuckDuckGo Instant Answers** via public API (no key needed)
- Exposes each as a distinct MCP “tool” for chatbots, agents, or local scripts

---

## 🚀 Why It Matters

- **One API to rule them all**  
  Call `google_search()`, `brave_search()`, or `duck_search()`, and get back ready‑to‑consume JSON without provider boilerplate.

- **Rapid tool development**  
  Spin up new search‑powered agents in minutes, not days.

- **Minimal key management**  
  Only Brave needs a key; DuckDuckGo works out‑of‑the‑box; Google key is optional.

- **Easy deployment**  
  Deploy via Docker or Smithery.ai with a single click.

---

For feedback or issues, join us on the Smithery Discord or open an issue in this repo.

