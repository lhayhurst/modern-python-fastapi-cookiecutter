from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.package_name}}.models import Base
from {{cookiecutter.package_name}}.main import app, get_db, settings


@pytest.fixture(autouse=True)
def setup_test_db(tmp_path):

    db_url = f"sqlite:///{tmp_path}test.db"

    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(name="client")
def test_client() -> TestClient:
    yield TestClient(app)


def test_read_users(client: TestClient):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_create_user(client: TestClient):
    data = {"email": "foobar@gmail.com"}
    response = client.post("/users/", json=data)
    assert response.status_code == 200

    response = client.get("/users/")
    response_data = response.json()
    assert len(response_data) == 1
    user = response_data[0]
    assert user["email"] == data["email"]
    assert "id" in user
    assert isinstance(user["id"], int)


def test_read_user(client: TestClient):
    data = {"email": "foobar@gmail.com"}
    client.post("/users/", json=data)

    response = client.get("/users/")
    response_data = response.json()
    user_id = response_data[0]["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert len(response_data) == 1
    user = response_data[0]
    assert user["email"] == data["email"]
    assert "id" in user
    assert isinstance(user["id"], int)
    assert user["id"] == user_id


def test_get_blog_posts_with_no_data(client: TestClient):
    response = client.get("/micro_blog_posts/")
    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.fixture(name="micro_blog_post_dict")
def micro_blog_post() -> dict:
    return {
        "title": "Birds are smarter than dogs, prove me wrong",
        "content": "While most people think that dogs are smarter than birds, scientific study has shown...",
    }


def test_create_blog_post_for_user(client: TestClient, micro_blog_post_dict):
    data = {"email": "foobar@gmail.com"}
    response = client.post("/users/", json=data)
    response_data = response.json()
    user_id = response_data["id"]

    response = client.post(f"/users/{user_id}/micro_blog_posts/", json=micro_blog_post_dict)
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    repo_id = response_data["id"]
    assert isinstance(repo_id, int)
    assert "user_id" in response_data
    assert response_data["user_id"] == user_id
    assert "title" in response_data
    assert response_data["title"] == micro_blog_post_dict["title"]
    assert "content" in response_data
    assert response_data["content"] == micro_blog_post_dict["content"]
