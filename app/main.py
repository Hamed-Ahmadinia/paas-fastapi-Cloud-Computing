print("### ASSIGNMENT 4 CODE LOADED ###")

import os
from fastapi import FastAPI, Header, HTTPException, Depends
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def require_api_key(x_api_key: str | None = Header(default=None, alias="X-API-Key")):
    expected = os.getenv("API_KEY")
    if not expected:
        raise HTTPException(status_code=500, detail="Server API_KEY not configured")

    if x_api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    return True

@app.get("/")
def root():
    return {"message": "Welcome! Public endpoint works."}

@app.get("/secret")
def secret(_: bool = Depends(require_api_key)):
    return {"secret": "This is protected data 🚫🔑"}
