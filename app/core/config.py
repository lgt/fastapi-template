import os
from typing import Optional
from pydantic import BaseModel


class Settings(BaseModel):
    API_TITLE: str = os.getenv("API_TITLE", "FastAPI Application")
    API_VERSION: str = os.getenv("API_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))


settings = Settings()
