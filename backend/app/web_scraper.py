import os
import requests
from dotenv import load_dotenv

load_dotenv()

def search_web(query: str):
    api_key = os.getenv("SERPER_API_KEY")
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "q": query
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        results = response.json().get("organic", [])[:5]
        return [f"{item.get('title', '')}: {item.get('snippet', '')}" for item in results]
    else:
        return [f"Web search failed with status {response.status_code}"]
