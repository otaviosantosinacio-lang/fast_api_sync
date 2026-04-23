import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from src.fast_api.app import app
from src.fast_api.models import table_registry

@pytest.fixture
def client():
    return TestClient(app=app)

@pytest.fixture
def session():
      engine = create_engine('sqlite:///:memory:')
      table_registry.metadata.create_all(engine)

      table_registry.metadata.drop_all(engine)