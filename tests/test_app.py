import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def register_and_login(username="testuser", password="testpass"):
    client.post("/auth/users/", json={"username": username, "password": password})
    resp = client.post("/auth/login/", json={"username": username, "password": password})
    token = resp.json()["access_token"]
    return token

def test_user_registration_and_login(test_db):
    resp = client.post("/auth/users/", json={"username": "hari", "password": "secret"})
    assert resp.status_code == 200
    assert resp.json()["username"] == "hari"

    resp = client.post("/auth/login/", json={"username": "hari", "password": "secret"})
    assert resp.status_code == 200
    assert "access_token" in resp.json()

def test_me_endpoint(test_db):
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.get("/auth/me/", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["username"] == "testuser"

def test_create_task(test_db):
    token = register_and_login("taskuser", "taskpass")
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.post("/tasks/", json={"title": "My Task", "description": "Do something"}, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "My Task"
    assert data["owner_id"] is not None

def test_update_task(test_db):
    token = register_and_login("updateuser", "updatepass")
    headers = {"Authorization": f"Bearer {token}"}
    # Create task
    resp = client.post("/tasks/", json={"title": "Old Title", "description": "Old desc"}, headers=headers)
    task_id = resp.json()["id"]

    # Update task
    resp = client.put(f"/tasks/{task_id}", json={"title": "New Title"}, headers=headers)
    assert resp.status_code == 200
    assert resp.json()["title"] == "New Title"

def test_list_tasks(test_db):
    token = register_and_login("listuser", "listpass")
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/tasks/", json={"title": "Task 1"}, headers=headers)
    client.post("/tasks/", json={"title": "Task 2"}, headers=headers)

    resp = client.get("/tasks/", headers=headers)
    assert resp.status_code == 200
    tasks = resp.json()
    assert len(tasks) >= 2
    assert all(task["owner_id"] is not None for task in tasks)
