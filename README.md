# MeteALOlogia-API
API service of the "MeteALOlogia" project. The project's goal is to create a weather station along with a website to view live measurements. This repository aims for creating an HTTP REST API server managing the collected data.

## Installation & Configuration
1. Use `poetry install` to install the dependencies.
2. `poetry shell` will spawn the virtual environment. Here you can set the environment variable `ENVFILE` to the path of a preferred configuration file. By default, it's `.env`, however there is no such file present in the repository by default. A sample development configuration is contained in `dev.env`.

    Schema of the stations is loaded from the yaml specified in the configuration file, under `STATIONS_SCHEMA`. It cannot be edited using REST. You can find a sample schema in `sample_stations.yaml`.
3. `poetry run start` runs the server according to the configuration. Endpoint documentation is available at `/docs`. 

## Testing
All tests are can be run using pytest on the `tests` directory. The configuration files (`test.env` and `test_stations.yaml`) have to be included in `PATH` during runtime, so the scripts are able to access them (eg. run pytest directly inside the directory).
