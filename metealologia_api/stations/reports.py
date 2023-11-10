from datetime import datetime
from hashlib import sha256
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Header, Response, Request, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

from ..config import Station, stations_schema
from ..database.models import ReportUpload
from ..database.session import database

station_key_header = APIKeyHeader(name="Authorization")


def get_station(station_id: str) -> Station | None:
    for station in stations_schema:
        if station.id == station_id:
            return station


def raise_nonexistent_station(station_id: str, station: Annotated[Station | None, Depends(get_station)]):
    if station is None:
        raise HTTPException(404, detail="station with id={} doesn't exist".format(station_id))


def check_authorization(station: Annotated[Station, Depends(get_station)],
                        station_key: Annotated[str, Security(station_key_header)]):
    if sha256(station_key.encode()).hexdigest() != station.key:
        raise HTTPException(403, detail="Invalid station key")


report_router = APIRouter(prefix="/{station_id}/sensors/{sensor_id}", dependencies=[Depends(raise_nonexistent_station)])


class ReportBody(BaseModel):
    timestamp: datetime
    data: dict


@report_router.post("/reports", status_code=201, response_class=Response, dependencies=[Depends(check_authorization)])
async def upload_report(station_id: str, sensor_id: str, body: ReportBody):
    """Uploads a new report"""
    await database.upload_report(
        ReportUpload(station_id=station_id, sensor_id=sensor_id, timestamp=body.timestamp, data=body.data)
    )


@report_router.get("/reports")
async def get_reports(station_id: str, sensor_id: str, after: datetime, before: datetime | None = None):
    """Fetches reports created after 'after' timestamp"""
    if before is None:
        before = datetime.now()
    return await database.get_reports(station_id, sensor_id, after, before)
