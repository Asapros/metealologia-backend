import importlib.metadata
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .atcs import atcs_router
from .config import settings
from .database.session import database
from .stations import stations_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect(settings.database_url)
    yield
    await database.disconnect()

app = FastAPI(debug=settings.environment == "development", lifespan=lifespan)
app.include_router(stations_router)
app.include_router(atcs_router)


@app.get("/")
async def main_route():
    """Runtime config"""
    return {
        "title": "MeteALOlogia",
        "version": importlib.metadata.version("metealologia_api"),
        "environment": settings.environment
    }



