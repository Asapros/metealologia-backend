from fastapi import APIRouter

from .reports import report_router
from ..config import stations_schema

stations_router = APIRouter(prefix="/stations")
stations_router.include_router(report_router)


@stations_router.get("")
async def get_all_stations():
    """Returns metadata of the all stations"""
    # TODO caching
    stations = []
    for station in stations_schema:
        station_dict = {"id": station.id, "name": station.name, "sensors": []}
        for sensor in station.sensors:
            station_dict["sensors"].append({"id": sensor.id, "name": sensor.name, "type": None, "lastUpdated": None})
        stations.append(station_dict)
    return stations
