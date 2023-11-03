from fastapi import APIRouter, HTTPException

report_router = APIRouter()


@report_router.post("/{station_id}/reports")
async def upload_report(station_id: str):
    """Uploads a new report"""
    raise HTTPException(status_code=501)


@report_router.get("/{station_id}/reports")
async def get_reports(station_id: str, after: int | None = None):
    """Fetches reports created after 'after' timestamp"""
    raise HTTPException(status_code=501)


@report_router.get("/{station_id}/listen")
async def listen_for_reports(stations_id: str):
    """Streams newly created reports"""
    raise HTTPException(status_code=501)