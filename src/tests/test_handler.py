import unittest
from apistar import test
from app import app

client = test.TestClient(app)


class TestHandler(unittest.TestCase):

    def test_welcome_handler(self):
        response = client.get('/')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json() == {"msg": "Welcome to API Star!"})
