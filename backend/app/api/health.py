from fastapi import APIRouter, Depends
from ..core.config import get_settings, Settings

router = APIRouter(tags=["system"])

@router.get("/health")
async def health(settings: Settings = Depends(get_settings)):
    return {"status": "ok", "app": settings.app_name, "version": settings.version}

@router.get("/live")
async def liveness():
    return {"alive": True}

@router.get("/ready")
async def readiness():
    # Placeholder for dependency checks (db, cache, etc.)
    return {"ready": True}
