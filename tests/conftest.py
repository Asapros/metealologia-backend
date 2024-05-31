import pytest
import yaml
from faker import Faker, Factory
from fastapi.testclient import TestClient

from metealologia_api import app

@pytest.fixture(scope="function")
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def faker():
    Faker.seed(2137)
    return Factory.create()


@pytest.fixture(scope="session")
def station_schema():
    with open("test_stations.yaml") as file:
        return yaml.safe_load(file)
