# PyTest REST API Example

This repo contains the sample code for the article - [Building and Testing FastAPI CRUD APIs with Pytest: A Step-By-Step Guide](https://pytest-with-eric.com/pytest-advanced/pytest-fastapi-testing/)

This project explains how to Build and Test A CRUD Rest API using FastAPI, SQLite (via SQLAlchemy) and Pytest.

# Requirements
* Python (3.10.9)

Please install the dependencies via the `requirements.txt` file using 
```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.

# How To Run the Unit Tests
To run the Unit Tests, from the root of the repo run
```commandline
pytest tests/unit/test_crud_api.py -v -s
```

If you have any questions about the project please raise an Issue on GitHub. 