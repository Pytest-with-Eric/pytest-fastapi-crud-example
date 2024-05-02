from fastapi.testclient import TestClient
from app.main import app
import uuid
import pytest


@pytest.fixture
def test_client():
    """Return a FastAPI test client instance."""
    yield TestClient(app)


@pytest.fixture
def user_id():
    """Generate a random user id."""
    return str(uuid.uuid4())


@pytest.fixture
def user_payload():
    """Generate a user payload."""
    return {
        "first_name": "PLACEHOLDER",
        "last_name": "PLACEHOLDER",
        "address": "PLACEHOLDER",
    }
