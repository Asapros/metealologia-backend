from fastapi import APIRouter

from .reports import report_router
from ..config import stations_schema

stations_router = APIRouter(prefix="/stations")
stations_router.include_router(report_router)


@stations_router.get("")
async def get_all_stations():
    """Returns metadata of the all stations"""
    # Caching
    return stations_schema
