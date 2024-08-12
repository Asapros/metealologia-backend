# MeteALOlogia-backend
Backend service of the "MeteALOlogia" project. The project's goal is to sustain weather stations and allow control of dedicated airships. Measurements and control panel will be accessible through a website. This repository is an HTTP REST API backend for it.

## Installation & Configuration
1. `poetry shell` will spawn the virtual environment.
2. Use `poetry install` to install the dependencies.
3. Set the environment variable `ENVFILE` to the path of a preferred configuration file. By default, it's `.env`, however there is no such file present in the repository by default. A sample development configuration is contained in `.env.dev`.
4. Schema of the stations is loaded from the yaml specified in the configuration file, under `STATIONS_SCHEMA`. It cannot be edited using REST. You can find a sample schema in `sample_stations.yaml`.
5. To create API keys for new stations use `poetry run key`. The command will generate a unique key and provide a hash ready to be copied to the stations schema file. For custom keys, the same command may be used in order to generate just the hash digest: `poetry run key <string>`.
    >    **Warning:** when using custom keys ensure proper length and randomness. Keys are not salted (nor peppered), making them prone to precomputed hash table type attacks. Meaningful tokens should **only** be used for demonstration purposes.

6. `poetry run start` runs the server according to the configuration. For basic runtime info see `/`. Endpoint documentation is available at `/docs`. 

## Deployment
Running with Docker will soon be documented here.

## Testing
All tests are can be run using pytest on the `tests` directory. The configuration files (`.env.test` and `test_stations.yaml`) have to be included in `PATH` during runtime, so the scripts are able to access them (eg. run pytest directly inside the directory).
