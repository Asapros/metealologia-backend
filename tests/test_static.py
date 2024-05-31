import importlib.metadata

import yaml


def test_main(client):
    assert client.get("/").json() == {
        "title": "MeteALOlogia",
        "version": importlib.metadata.version("metealologia_api"),
        "environment": "test"
    }


def test_stations(client, station_schema):
    for station in station_schema:
        del station["key"]
    assert station_schema == client.get("/stations").json()