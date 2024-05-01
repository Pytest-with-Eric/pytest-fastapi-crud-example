from fastapi.testclient import TestClient
from app.main import app
import uuid
import pytest


@pytest.fixture
def test_client():
    """Return a FastAPI test client instance."""
    yield TestClient(app)


@pytest.fixture
def user_id(scope="session"):
    """Generate a random user id."""
    return str(uuid.uuid4())


@pytest.fixture
def user_payload(user_id):
    """Generate a user payload."""
    return {
        "id": user_id,
        "first_name": "PLACEHOLDER",
        "last_name": "PLACEHOLDER",
        "address": "PLACEHOLDER",
        "createdAt": "2024-04-30T16:39:23",
    }
