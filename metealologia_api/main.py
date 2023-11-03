import importlib.metadata

import uvicorn

from . import app
from .config import settings


@app.get("/")
async def main_route():
    return {
        "title": "MeteALOlogia",
        "version": importlib.metadata.version("metealologia_api"),
        "environment": settings.environment
    }


def start():
    uvicorn.run("metealologia_api.main:app", host="localhost", port=8080, reload=settings.environment == "development")
