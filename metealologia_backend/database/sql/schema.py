from sqlalchemy import Column, DateTime, JSON, MetaData, Table, String

metadata = MetaData()

reports = Table(
    "reports",
    metadata,
    Column("station_id", String),
    Column("sensor_id", String),
    Column("timestamp", DateTime),
    Column("data", JSON)
)