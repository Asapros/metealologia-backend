import importlib.metadata
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from metealologia_backend.config import settings
from metealologia_backend.database.session import database
from metealologia_backend.stations import stations_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect(settings.database_url)
    yield
    await database.disconnect()

app = FastAPI(debug=settings.environment == "development", lifespan=lifespan, root_path=settings.root_path)
app.include_router(stations_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main_route():
    """Runtime config"""
    return {
        "repository_url": importlib.metadata.metadata("metealologia_backend")["Home-Page"],
        "title": importlib.metadata.metadata("metealologia_backend")["Name"],
        "version": importlib.metadata.version("metealologia_backend"),
        "environment": settings.environment
    }



