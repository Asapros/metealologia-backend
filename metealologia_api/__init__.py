from fastapi import FastAPI

from .config import settings
from .database.session import database
from .stations import stations_router

app = FastAPI(debug=settings.environment == "development")
app.include_router(stations_router)


@app.on_event("startup")
async def startup():
    await database.connect(settings.database_url)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()