# User Service API Example

## Overview

This is a simple User Service CRUD (Create, Read, Update, Delete) API built with FastAPI and SQLite. The API allows you to create, read, update, and delete users. It uses Pydantic models for request and response validation and SQLAlchemy for database operations.

## Architecture
This project follows a clean architecture pattern, separating concerns to enhance maintainability and scalability. Here's a brief overview:

- API Layer (FastAPI): Handles HTTP requests and responses, routing, and interaction with the service layer.
- Service Layer: Contains business logic and communicates with the database layer.
- Database Layer (SQLite): Manages data persistence and database operations.
- Testing: Unit tests are written in Pytest to test the service layer functions.

## Getting Started

### Prerequisites and Dependencies
- Python 3.12
- FastAPI
- SQLite
- Uvicorn (for running the server)

#### Poetry

This project uses [Poetry](https://python-poetry.org/) for dependency management. 

If you're not familiar with Poetry, please follow [these instructions](https://python-poetry.org/docs/#installation) to install it.

Once you've installed Poetry, you can install the dependencies using the following command:

```shell
$ poetry install
```

Then run the below command to activate the virtual environment.

```shell
$ poetry shell
```

#### Pip

If you prefer using `pip`, you can create a virtual environment and then install the dependencies using the following command:

```shell
$ pip install -r requirements.txt
```

## How To Run the Server

To run the server, use the following command:

```shell
$ uvicorn app.main:app --host localhost --port 8000 --reload
```

This will spin up the server at `http://localhost:8000` with a local SQLite database `users.db`.

## API Endpoints

### Create User

- `POST /api/users/`: Create a new user.

To create a user, send a POST request to `http://localhost:8000/api/users` with the following JSON payload:

```json
{
    "first_name": "John",
    "last_name": "Doe",
    "address": "123 Fake St",
    "activated": true
}
```

As we use Pydantic models, the API will validate the request payload and return an error if the payload is invalid.

### Get Users

- `GET /api/users/`: Get all users.

To get all users, send a GET request to `http://localhost:8000/api/users`.

### Get User by ID

- `GET /api/users/{userId}/`: Get a user by ID.

To get a user by ID, send a GET request to `http://localhost:8000/api/users/{userId}`. 

If the user with the specified ID does not exist, the API will return a 404 Not Found response. The same logic is carried out for the Update and Delete endpoints.


### Update User

- `PATCH /api/users/{userId}/`: Update a user by ID.

To update a user by ID, send a PATCH request to `http://localhost:8000/api/users/{userId}` with the following JSON payload:

```json
{
    "first_name": "Jane",
    "last_name": "Doe",
    "address": "321 Fake St",
    "activated": true
}
```

### Delete User

- `DELETE /api/users/{userId}/`: Delete a user by ID.

To delete a user by ID, send a DELETE request to `http://localhost:8000/api/users/{userId}`.

## How To Run the Unit Tests
To run the Unit Tests, from the root of the repo run
```shell
$ pytest 
```

This will spin up a test database in SQLite `test_db.db`, run the tests and then tear down the database. 

You can use `pytest -v` for verbose output and `pytest -s` to disable output capture for better debugging.