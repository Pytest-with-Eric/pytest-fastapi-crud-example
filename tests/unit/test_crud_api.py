from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

user_id = str(uuid.uuid4())


def test_root():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}


def test_create_user():
    sample_payload = {
        "id": user_id,
        "first_name": "PLACEHOLDER",
        "last_name": "PLACEHOLDER",
        "address": "PLACEHOLDER",
        "activated": False,
        "createdAt": "2023-03-17T00:04:32",
    }
    response = client.post("/api/users/", json=sample_payload)
    assert response.status_code == 201
    assert response.json() == {
        "Status": "Success",
        "User": {
            "first_name": "PLACEHOLDER",
            "last_name": "PLACEHOLDER",
            "activated": False,
            "createdAt": "2023-03-17T00:04:32",
            "id": user_id,
            "address": "PLACEHOLDER",
            "updatedAt": None,
        },
    }


def test_get_user():
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {
        "Status": "Success",
        "User": {
            "first_name": "PLACEHOLDER",
            "last_name": "PLACEHOLDER",
            "activated": False,
            "createdAt": "2023-03-17T00:04:32",
            "address": "PLACEHOLDER",
            "id": user_id,
            "updatedAt": None,
        },
    }


def test_update_user():
    sample_payload = {
        "id": user_id,
        "first_name": "PLACEHOLDER2",
        "last_name": "PLACEHOLDER2",
        "address": "PLACEHOLDER2",
        "activated": True,
        "createdAt": "2023-03-17T00:04:32",
        "updatedAt": "2023-03-17T00:06:32",
    }
    response = client.patch(f"/api/users/{user_id}", json=sample_payload)
    assert response.status_code == 202
    assert response.json() == {
        "Status": "Success",
        "User": {
            "first_name": "PLACEHOLDER2",
            "last_name": "PLACEHOLDER2",
            "activated": True,
            "createdAt": "2023-03-17T00:04:32",
            "id": user_id,
            "address": "PLACEHOLDER2",
            "updatedAt": "2023-03-17T00:06:32",
        },
    }


def test_delete_user():
    response = client.delete(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {
        "Status": "Success",
        "Message": "User deleted successfully",
    }


def test_get_user_not_found():
    response = client.get(
        f"/api/users/16303002-876a-4f39-ad16-e715f151bab3"
    )  # GUID not in DB
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No User with this id: `16303002-876a-4f39-ad16-e715f151bab3` found"
    }
