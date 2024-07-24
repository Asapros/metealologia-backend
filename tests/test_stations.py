from datetime import timedelta

import pytest


@pytest.fixture(scope="session")
def sensor_paths(station_schema) -> list[str]:
    generated = []
    path = "/stations/{}/sensors/{}/reports"
    for station in station_schema:
        for sensor in station["sensors"]:
            generated.append(path.format(station["id"], sensor["id"]))
    return generated


@pytest.fixture(scope="session")
def station_keys():
    return ["sample", None]


def test_invalid_sensor_get(client, faker, station_schema, sensor_paths):
    path = sensor_paths[0]
    station_id = station_schema[0]["id"]
    sensor_id = station_schema[0]["sensors"][0]["id"]
    assert client.get(path.replace(station_id, faker.word())).status_code == 404
    assert client.get(path.replace(sensor_id, faker.word())).status_code == 404
    assert client.get(path, params={"limit": 51}).status_code == 422
    assert client.get(path, params={"after": faker.word()}).status_code == 422


def test_invalid_sensor_post(client, sensor_paths, faker, station_keys):
    path = sensor_paths[0]
    station_key = station_keys[0]

    assert client.post(path, headers={"Authorization": faker.word()}).status_code == 403
    assert client.post(path, headers={"Authorization": station_key}, content=faker.sentence()).status_code == 422
    assert client.post(path, headers={"Authorization": station_key},
                       json={"timestamp": faker.word(), "data": {}}).status_code == 422


def test_sensor_store(client, sensor_paths, station_keys, faker):
    path = sensor_paths[0]
    station_key = station_keys[0]
    measurement_date = faker.date_time_this_century()
    measurement = {faker.word(): faker.pyint(), faker.word(): faker.sentence(), faker.word(): faker.pyfloat()}
    payload = {
        "timestamp": measurement_date.isoformat(),
        "data": measurement
    }
    assert client.post(path, headers={"Authorization": station_key}, json=payload).is_success
    assert len(client.get(path, params={"after": measurement_date + timedelta(days=1)}).json()) == 0
    assert client.get(path, params={"after": measurement_date - timedelta(days=1)}).json() == [payload]
    assert len(client.get(path, params={"after": measurement_date - timedelta(days=2),
                                        "before": measurement_date - timedelta(days=1)}).json()) == 0
    assert client.get(path, params={"after": measurement_date - timedelta(days=2),
                                    "before": measurement_date + timedelta(days=1)}).json() == [payload]

    for iter_path in sensor_paths:
        if iter_path == path:
            continue
        assert len(client.get(iter_path, params={"after": 0}).json()) == 0
