from datetime import datetime

from pydantic import BaseModel


class ReportData(BaseModel):
    timestamp: datetime
    data: dict


class Report(ReportData):
    station_id: str
    sensor_id: str


class ReportUpload(Report):
    pass
