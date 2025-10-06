import unittest
import requests
import json
import uuid


class TestMondoDocuments(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.base_url = "http://localhost"
        self.signup_url = f"{self.base_url}/auth/signup"
        self.sign_in = f"{self.base_url}/auth/token?grant_type=password"

        self.economics = f"{self.base_url}/api/items/economic"
        self.headers = {
            "Content-Type": "application/json"
        }

        email = f"{str(uuid.uuid4())}@example.com"
        self.payload = {
            "email": email,
            "password": "strongpassword"
        }

        response = requests.post(
            self.signup_url,
            headers=self.headers,
            data=json.dumps(self.payload)
        )

        # Assert successful response
        self.assertEqual(response.status_code, 200)  # Or 200 depending on your API

        # Check response content (adjust based on your API response)
        response_data = response.json()

        self.assertIn("user", response_data)
        response_use = response_data['user']
        self.assertIn("email", response_use)
        self.assertEqual(response_use["email"], email)

        response_sign_in = requests.post(self.sign_in, headers=self.headers, json=self.payload)

        self.assertIn("access_token", response_sign_in.json())

        access_token = response_sign_in.json()["access_token"]

        # Create session
        self.session = requests.session()

        # Set headers including authorization
        self.session.headers.update({
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        })

    def test_succesful_check_auth_call(self):
        """Test successful user signup"""

        response_sign_in = requests.post(self.sign_in, headers=self.headers, json=self.payload)

        self.assertIn("access_token", response_sign_in.json())

        result = self.session.get(url=self.economics)

        self.assertEqual(200, result.status_code)

        open('docs.json','w+').write(json.dumps(result.json()))

    def tearDown(self):
        """Clean up after each test"""
        # Add any cleanup code here if needed
        # For example, delete test users from database
        pass


if __name__ == '__main__':
    # Run with more verbose output
    unittest.main(verbosity=2)

    # Alternative: Run specific test
    # unittest.main(defaultTest='TestSignupAPI.test_successful_signup')
