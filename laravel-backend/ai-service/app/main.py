from fastapi import FastAPI
from app.schemas.health import HealthResponse
from app.core.config import settings

app = FastAPI(title="ResumeFit AI Service")

@app.get("/", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        service="ResumeFit AI Service",
        status="running"
    )