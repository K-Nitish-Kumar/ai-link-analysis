from fastapi import FastAPI
from app.schemas import Request, Response
from app.services.analysis_service import run
import logging
logging.basicConfig(level=logging.INFO)
app = FastAPI(title="ai-link-analysis", version="1.0.0")
@app.get("/")
def health():
    return {"status":"ok", "docs":"/docs"}
@app.post("/link-analysis", response_model=Response)
def endpoint(body: Request):
    return run(body)
