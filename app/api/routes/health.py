from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "fastapi-app"
    }

@router.get("/health/ready")
async def readiness_check():
    return {
        "status": "ready",
        "service": "fastapi-app"
    }
