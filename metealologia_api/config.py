from pydantic import BaseModel, TypeAdapter
from pydantic_settings import BaseSettings, SettingsConfigDict
import yaml


class Settings(BaseSettings):
    environment: str
    database_url: str
    database_flavour: str
    stations_schema: str
    host: str
    port: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


class Sensor(BaseModel):
    id: str
    name: str
    type: str


class Station(BaseModel):
    id: str
    name: str
    sensors: list[Sensor]


_StationsType = TypeAdapter(list[Station])

with open(settings.stations_schema) as file:
    stations_schema = _StationsType.validate_python(yaml.safe_load(file))
