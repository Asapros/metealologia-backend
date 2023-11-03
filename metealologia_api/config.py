from pydantic import BaseModel, TypeAdapter
from pydantic_settings import BaseSettings, SettingsConfigDict
import yaml


class Settings(BaseSettings):
    environment: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


class Sensor(BaseModel):
    id: str
    name: str


class Station(BaseModel):
    id: str
    name: str
    sensors: list[Sensor]


_StationsType = TypeAdapter(list[Station])

with open("stations.yaml") as file:
    stations_schema = _StationsType.validate_python(yaml.safe_load(file))
