from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.chains import run_fact_check

app = FastAPI()

# Enable frontend/backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Misinfo Guard API is live!"}

@app.post("/fact-check")
async def fact_check(request: Request):
    body = await request.json()
    query = body.get("query")
    if not query:
        return {"error": "No query provided"}
    result = run_fact_check(query)
    return {"result": result}
