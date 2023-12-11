from fastapi.testclient import TestClient
from main import app
from main import Msg

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World. Welcome to the API home page!"}

def test_function_demo_get():
    response = client.get("/path")
    assert response.status_code == 200
    assert response.json() == {"message": "This is /path endpoint, use post request to transform text to uppercase"}

def test_function_demo_post():
    data = {"msg": "hello"}
    response = client.post("/path", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "HELLO"}

def test_function_demo_get_path_id():
    response = client.get("/path/123")
    assert response.status_code == 200
    assert response.json() == {"message": "This is /path/123 endpoint, use post request to retrieve result"}
