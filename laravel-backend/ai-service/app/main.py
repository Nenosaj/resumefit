from fastapi import FastAPI

app = FastAPI(title="ResumeFit AI Service", version="0.1.0")

@app.get("/")
async def health_check():
    return {"service": "ResumeFit AI Service", "status": "ok", "version": app.version}