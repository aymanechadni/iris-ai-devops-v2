
from fastapi import FastAPI

app = FastAPI(
    title="Application IA DevOps V2",
    version="2.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Version 2 - Application IA DevOps",
        "status": "running",
        "model": "Random Forest",
        "version": "2.0.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
