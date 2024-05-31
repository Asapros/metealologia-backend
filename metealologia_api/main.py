import uvicorn

from .config import settings


def start():
    uvicorn.run(
        "metealologia_api:app",
        host=settings.host,
        port=settings.port,
        reload=settings.environment == "development"
    )
