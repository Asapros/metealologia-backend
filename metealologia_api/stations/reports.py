from datetime import datetime
from hashlib import sha256
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

from ..config import Station, api_key_hashes, stations_schema
from ..database.models import ReportData, ReportUpload
from ..database.session import database

station_key_header = APIKeyHeader(name="Authorization")


def validate_sensor(station_id: str, sensor_id: str) -> Station | None:
    for station in stations_schema:
        if station.id == station_id:
            for sensor in station.sensors:
                if sensor.id == sensor_id:
                    return
            raise HTTPException(404, detail="Sensor with id={} doesn't exist on station id={}".format(sensor_id, station_id))
    raise HTTPException(404, detail="Station with id={} doesn't exist".format(station_id))


def check_authorization(station_id: str, station_key: Annotated[str, Security(station_key_header)]):
    if sha256(station_key.encode()).hexdigest() != api_key_hashes[station_id]:
        raise HTTPException(403, detail="Invalid station key")


report_router = APIRouter(prefix="/{station_id}/sensors/{sensor_id}", dependencies=[Depends(validate_sensor)])


class ReportBody(BaseModel):
    timestamp: datetime
    data: dict


@report_router.post("/reports", status_code=201, response_class=Response, responses={403: {"description": "Invalid API key"}}, dependencies=[Depends(check_authorization)])
async def upload_report(station_id: str, sensor_id: str, body: ReportBody):
    """Uploads a new report"""
    await database.upload_report(
        ReportUpload(station_id=station_id, sensor_id=sensor_id, timestamp=body.timestamp, data=body.data)
    )


@report_router.get("/reports", response_model=list[ReportData], responses={404: {"description": "Station not found"}})
async def get_reports(station_id: str, sensor_id: str, after: datetime, before: datetime | None = None):
    """Fetches reports created between 'after' and 'before' timestamps"""
    if before is None:
        before = datetime.now()
    return await database.get_reports(station_id, sensor_id, after, before)
