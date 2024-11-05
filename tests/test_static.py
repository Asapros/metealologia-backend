import importlib.metadata

import yaml


def test_main(client):
    assert client.get("/").json() == {
        "repository_url": "https://github.com/Asapros/metealologia-backend",
        "title": importlib.metadata.metadata("metealologia_backend")["Name"],
        "version": importlib.metadata.version("metealologia_backend"),
        "environment": "test"
    }


def test_stations(client, station_schema):
    for station in station_schema:
        del station["key"]
    assert station_schema == client.get("/stations").json()