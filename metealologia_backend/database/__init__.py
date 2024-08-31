from abc import ABC, abstractmethod
from datetime import datetime

from metealologia_backend.database.models import Report, ReportData, ReportUpload


class Database(ABC):
    @abstractmethod
    async def connect(self, database_url: str):
        pass

    @abstractmethod
    async def disconnect(self):
        pass

    @abstractmethod
    async def upload_report(self, report: ReportUpload):
        pass

    @abstractmethod
    async def get_reports(self, station_id: str, sensor_id: str, after: datetime, before: datetime, limit: int) -> list[ReportData]:
        pass
