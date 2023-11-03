import importlib.metadata

import uvicorn
from fastapi import FastAPI

from .config import settings

app = FastAPI()


@app.get("/")
async def main_route():
    return "MeteALOlogia API v{}".format(importlib.metadata.version("metealologia_api"))


@app.get("/env")
async def env_route():
    return "env: {}".format(settings.environment)


def start():
    uvicorn.run("metealologia_api.main:app", host="localhost", port=8000, reload=settings.environment == "development")
