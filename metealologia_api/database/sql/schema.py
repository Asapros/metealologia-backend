from sqlalchemy import Column, DateTime, Integer, JSON, MetaData, Table, String

metadata = MetaData()

reports = Table(
    "reports",
    metadata,
    Column("station_id", String),
    Column("sensor_id", String),
    Column("timestamp", DateTime),
    Column("data", JSON)
)