from fastapi import FastAPI

from .stations import stations_router

app = FastAPI()
app.include_router(stations_router)