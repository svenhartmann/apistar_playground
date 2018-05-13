from apistar import test
from app import app


client = test.TestClient(app)

def test_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to API Star!"}
