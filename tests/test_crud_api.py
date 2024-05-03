import time


def test_root(test_client):
    response = test_client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}


def test_create_user(test_client, user_payload):
    print(user_payload)
    response = test_client.post("/api/users/", json=user_payload)
    response_json = response.json()
    assert response.status_code == 201
    assert response_json["Status"] == "Success"
    assert response_json["User"]["id"] == user_payload["id"]
    assert response_json["User"]["address"] == "123 Farmville"
    assert response_json["User"]["first_name"] == "John"
    assert response_json["User"]["last_name"] == "Doe"


# def test_get_user(test_client, user_id):
#     response = test_client.get(f"/api/users/{user_id}")
#     response_json = response.json()
#     assert response.status_code == 200
#     assert response_json["Status"] == "Success"
#     assert response_json["User"]["id"] == user_id
#     assert response_json["User"]["address"] == "123 Farmville"
#     assert response_json["User"]["first_name"] == "John"
#     assert response_json["User"]["last_name"] == "Doe"


# def test_update_user(test_client, user_id, user_payload_updated):
#     time.sleep(
#         1
#     )  # Sleep for 1 second to ensure updatedAt is different (datetime precision is low in SQLite)
#     response = test_client.patch(f"/api/users/{user_id}", json=user_payload_updated)
#     response_json = response.json()
#     assert response.status_code == 202
#     assert response_json["Status"] == "Success"
#     assert response_json["User"]["id"] == user_id
#     assert response_json["User"]["address"] == "321 Farmville"
#     assert response_json["User"]["first_name"] == "Jane"
#     assert response_json["User"]["last_name"] == "Doe"
#     assert response_json["User"]["activated"] is True
#     assert (
#         response_json["User"]["updatedAt"] is not None
#         and response_json["User"]["updatedAt"] > response_json["User"]["createdAt"]
#     )


# def test_delete_user(test_client, user_id):
#     response = test_client.delete(f"/api/users/{user_id}")
#     assert response.status_code == 200
#     assert response.json() == {
#         "Status": "Success",
#         "Message": "User deleted successfully",
#     }

#     # Try to get the deleted user
#     response = test_client.get(f"/api/users/{user_id}")
#     assert response.status_code == 404
#     assert response.json() == {"detail": f"No User with this id: `{user_id}` found"}


# # def test_get_users(test_client, user_payload, user_payload2):
# #     response1 = test_client.post("/api/users/", json=user_payload)
# #     assert response1.status_code == 201

# #     # Add a second user
# #     response2 = test_client.post("/api/users/", json=user_payload2)
# #     assert response2.status_code == 201

# #     # Get all users
# #     response = test_client.get("/api/users/")
# #     response_json = response.json()
# #     assert response.status_code == 200
# #     assert response_json["status"] == "Success"
# #     assert response_json["results"] == 2
