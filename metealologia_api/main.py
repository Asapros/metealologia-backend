import importlib.metadata

import uvicorn

from . import app
from .config import settings


@app.get("/")
async def main_route():
    """Runtime config"""
    return {
        "title": "MeteALOlogia",
        "version": importlib.metadata.version("metealologia_api"),
        "environment": settings.environment
    }


def start():
    uvicorn.run("metealologia_api.main:app", host=settings.host, port=settings.port, reload=settings.environment == "development")
