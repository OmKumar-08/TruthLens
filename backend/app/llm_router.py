import os
import requests
from dotenv import load_dotenv


load_dotenv()

def query_llm(prompt: str):
    headers={
        "Authorization":f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type":"application/json"

    }

    data={
        "model": os.getenv("OPENROUTER_MODEL","mistralai/mistral-7b-instruct"),
        "messages":[{"role":"user","content":prompt}]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]