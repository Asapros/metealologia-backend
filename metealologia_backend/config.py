from os import getenv, path

import yaml
from pydantic import BaseModel, TypeAdapter, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

env_file = getenv("ENVFILE", None)
if env_file is not None and not path.exists(env_file):
    raise RuntimeError("Specified ENVFILE '{}' not found.".format(env_file))


class Settings(BaseSettings):
    environment: str
    database_url: str
    database_flavour: str
    stations_schema: str
    report_limit: int
    cors_origins: list[str]
    host: str
    port: int
    logging_config: str
    root_path: str = ""

    model_config = SettingsConfigDict(env_file=env_file)

try:
    settings = Settings()
except ValidationError as error:
    reasons = []
    for reason in error.errors():
        reasons.append("- {}: {}".format(reason["loc"][0].upper(), reason["msg"]))

    location = "loaded .env file '{}' and/or ".format(env_file)
    raise RuntimeError(
        "{}environment variables contain {} error{}:\n{}".format(
            location if env_file is not None else "",
            error.error_count(),
            "s" if error.error_count() > 1 else "", "\n".join(reasons)
        ).capitalize()
    ) from error

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
