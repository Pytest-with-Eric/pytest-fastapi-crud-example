import uuid
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
note_id = str(uuid.uuid4())


def test_root():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI with SQLAlchemy"}


def test_get_notes():
    response = client.get("/api/notes/")
    assert response.status_code == 200
    assert response.json() == {'status': 'success', 'results': 0, 'notes': []}


def test_create_note():
    sample_payload = {
          "id": note_id,
          "title": "string",
          "content": "string",
          "category": "string",
          "published": False,
          "createdAt": "2023-03-14T09:11:48.620Z",
          "updatedAt": "2023-03-14T09:11:48.620Z"
        }
    response = client.post("/api/notes/", json=sample_payload)
    print(response.json())
    assert response.status_code == 201
    assert response.json() == {'status': 'success', 'note': {'published': False, 'title': 'string', 'content': 'string', 'createdAt': '2023-03-14T09:11:48.620000', 'id': note_id, 'category': 'string', 'updatedAt': '2023-03-14T09:11:48.620000'}}

