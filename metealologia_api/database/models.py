from datetime import datetime

from pydantic import BaseModel


class ReportBase(BaseModel):
    station_id: str
    sensor_id: str
    timestamp: datetime
    data: dict


class Report(ReportBase):
    pass


class ReportUpload(ReportBase):
    pass
