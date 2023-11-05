from datetime import datetime

from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel

from ..database.models import ReportUpload
from ..database.session import database

report_router = APIRouter(prefix="/{station_id}/sensor/{sensor_id}")


class ReportBody(BaseModel):
    timestamp: datetime
    data: dict


@report_router.post("/reports", status_code=201, response_class=Response)
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


@report_router.get("/listen")
async def listen_for_reports(stations_id: str):
    """Streams newly created reports"""
    raise HTTPException(status_code=501)