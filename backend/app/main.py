from fastapi import FastAPI
from .core.config import get_settings
from .api import health
from .core.logging import logger

settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.version)

app.include_router(health.router, prefix="/api/v3")

@app.on_event("startup")
async def on_startup():
    logger.info({"event": "startup", "app": settings.app_name, "env": settings.environment})

@app.on_event("shutdown")
async def on_shutdown():
    logger.info({"event": "shutdown"})

@app.get("/")
async def root():
    return {"message": "SCOUT Backend API", "version": settings.version}
