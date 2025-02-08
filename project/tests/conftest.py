import os
import pytest
from starlette.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer
from app import main
from app.config import get_settings, Settings

def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))

@pytest.fixture(scope="module")
def test_app():
    # set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    initializer(["app.models.tortoise"], db_url=os.environ.get("DATABASE_TEST_URL"))
    with TestClient(main.app) as test_client:
        # testing
        yield test_client
    # tear down
    finalizer()