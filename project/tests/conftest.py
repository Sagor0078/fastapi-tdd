import os
import pytest
from starlette.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer
from app.main import app
from app.config import get_settings, Settings

def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))

@pytest.fixture(scope="module")
def test_app():
    # Initialize test database
    initializer(["app.models.tortoise"], db_url=os.environ.get("DATABASE_TEST_URL"))

    # Override dependencies
    app.dependency_overrides[get_settings] = get_settings_override

    # Use TestClient
    with TestClient(app) as test_client:
        yield test_client  # Run tests

    # Cleanup database after tests
    finalizer()
