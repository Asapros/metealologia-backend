# MeteALOlogia-backend
Backend service of the "MeteALOlogia" project. The project's goal is to sustain weather stations and allow control of dedicated airships. Measurements and control panel will be accessible through a website. This repository is an HTTP REST API backend for it.

## Run locally
1. Installation
   1. First ensure you have python poetry installed.
   2. `poetry shell` will spawn the virtual environment.
   3. Use `poetry install` to install the dependencies.
2. Configuration
   1. Set the environment variable `ENVFILE` to the path of a preferred configuration file. A sample development configuration is contained in `.env.development`.
   2. Schema of the stations is loaded from the YAML specified in the configuration file, under `STATIONS_SCHEMA`. It cannot be edited using REST. You can find a sample schema in `sample_stations.yaml`.
   3. To create API keys for new stations use `poetry run key`. The command will generate a unique key and provide a hash ready to be copied to the stations schema file. For custom keys, the same command may be used in order to generate just the hash digest: `poetry run key <string>`.
   >  **Warning:** when using custom keys ensure proper length and randomness. Keys are not salted (nor peppered), making them prone to precomputed hash table type attacks. Meaningful tokens should **only** be used for demonstration purposes.

3. `poetry run start` runs the server according to the configuration. For basic runtime info see `/`. Endpoint documentation is available at `/docs`. 

## Testing
All tests are can be run using pytest on the `tests` directory. The configuration files (`.env.test` and `test_stations.yaml`) have to be included in `PATH` during runtime, so the scripts are able to access them (eg. run pytest directly inside the directory).

## Deployment
1. Build the image with docker.
2. Run the image. Remember to apply following options:
   - Bind desired port to 80 in the container.
   - Bind stations configuration file.
   - Set all required environment variables.
      - Alternatively you can bind `.env` file to a place inside the container and set just ENVFILE variable to that path.
   - When using sqlite database implementation, bind a volume to the place you're storing the database in.
