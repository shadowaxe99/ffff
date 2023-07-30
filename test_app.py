import unittest
from app import app, db


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # This method will be called before each test
        self.app = app.test_client()
        self.db = db

    def tearDown(self):
        # This method will be called after each test
        pass

    def test_home_page(self):
        # Send a GET request to the app and assert the response
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        # Send a POST request to the app to create a new user and assert the response
        response = self.app.post('/user', json={"username": "test", "email": "test@example.com"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["message"], "User created successfully.")


if __name__ == '__main__':
    unittest.main()
