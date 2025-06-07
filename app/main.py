from fastapi import FastAPI
import fastapi
from api.routes.health import router as health_router
from core.config import settings

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    debug=settings.DEBUG
)

# Include routers
app.include_router(health_router, prefix="/api/v1")

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to FastAPI!",
        "version": settings.API_VERSION,
        "fastapi_version": fastapi.__version__,
        "docs": "/docs"
    }