from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_success():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_hello_fail():
    response = client.get("/hello-wrong")
    assert response.status_code == 404
