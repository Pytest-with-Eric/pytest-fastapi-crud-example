def test_root(test_client):
    response = test_client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}


def test_create_user_success(test_client, user_payload, user_id):
    response = test_client.post("/api/users/", json=user_payload)
    assert response.status_code == 201
    assert response.json() == {
        "Status": "Success",
        "User": {
            "id": user_id,
            "activated": False,
            "createdAt": "2024-04-30T16:39:23",
            "first_name": "PLACEHOLDER",
            "last_name": "PLACEHOLDER",
            "address": "PLACEHOLDER",
            "updatedAt": None,
        },
    }


# def test_create_user_fail(test_client, user_payload, user_id):
#     response = test_client.post("/api/users/", json=user_payload)
#     assert response.status_code == 400
#     assert response.json() == {
#         "detail": "User with id: `16303002-876a-4f39-ad16-e715f151bab3` already exists"
#     }


# def test_get_user(test_client):
#     response = test_client.get(f"/api/users/{user_id}")
#     assert response.status_code == 200
#     assert response.json() == {
#         "Status": "Success",
#         "User": {
#             "first_name": "PLACEHOLDER",
#             "last_name": "PLACEHOLDER",
#             "activated": False,
#             "createdAt": "2023-03-17T00:04:32",
#             "address": "PLACEHOLDER",
#             "id": user_id,
#             "updatedAt": None,
#         },
#     }


# def test_update_user(test_client, sample_payload):
#     response = test_client.patch(f"/api/users/{user_id}", json=sample_payload)
#     assert response.status_code == 202
#     assert response.json() == {
#         "Status": "Success",
#         "User": {
#             "first_name": "PLACEHOLDER2",
#             "last_name": "PLACEHOLDER2",
#             "activated": True,
#             "createdAt": "2023-03-17T00:04:32",
#             "id": user_id,
#             "address": "PLACEHOLDER2",
#             "updatedAt": "2023-03-17T00:06:32",
#         },
#     }


# def test_delete_user(test_client):
#     response = test_client.delete(f"/api/users/{user_id}")
#     assert response.status_code == 200
#     assert response.json() == {
#         "Status": "Success",
#         "Message": "User deleted successfully",
#     }


# def test_get_user_not_found(test_client):
#     response = test_client.get(
#         f"/api/users/16303002-876a-4f39-ad16-e715f151bab3"
#     )  # GUID not in DB
#     assert response.status_code == 404
#     assert response.json() == {
#         "detail": "No User with this id: `16303002-876a-4f39-ad16-e715f151bab3` found"
#     }
