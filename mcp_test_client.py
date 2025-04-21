import requests
import json

# Your Google API Key and Custom Search Engine ID
api_key = "YOUR_GOOGLE_API_KEY"
#cse_id  = "YOUR_CUSTOM_SEARCH_ENGINE_ID"

# Build request params
params = {
    "key": api_key,
    "q":   "Bengal Riots in April 2025",  # your query
    "num": 10                              # max 10 results per request
}

# Google Custom Search API endpoint
url = "https://www.googleapis.com/customsearch/v1"

# Send the GET request
response = requests.get(url, params=params)

# Check for success and pretty‑print JSON
if response.status_code == 200:
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error {response.status_code}: {response.text}")
