from os import getenv, path

from pydantic import BaseModel, TypeAdapter
from pydantic_settings import BaseSettings, SettingsConfigDict
import yaml

env_file = getenv("ENVFILE", ".env")
if not path.exists(env_file):
    raise RuntimeError("Environment file '{}' not found.".format(env_file))


class Settings(BaseSettings):
    environment: str
    database_url: str
    database_flavour: str
    stations_schema: str
    report_limit: int
    frontend_address: str
    host: str
    port: int

    model_config = SettingsConfigDict(env_file=env_file)


settings = Settings()


class Sensor(BaseModel):
    id: str
    name: str
    type: str


class Station(BaseModel):
    id: str
    name: str
    sensors: list[Sensor]


class StationConfig(Station):
    key: str


_StationsType = TypeAdapter(list[StationConfig])

with open(settings.stations_schema) as file:
    _config = _StationsType.validate_python(yaml.safe_load(file))

stations_schema = [Station(**station_config.model_dump()) for station_config in _config]
api_key_hashes = {station_config.id: station_config.key for station_config in _config}
