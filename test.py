import unittest
from unittest.mock import Mock, patch
import json
import requests
from services import create_user
from constants import BASE_URL2


class APITest(unittest.TestCase):
    def test_api(self):
        r = requests.get(BASE_URL2)
        self.assertEqual(r.status_code, 200)


    @patch('services.requests.post')
    def test_create_user(self, mock_post):
        mock_post.return_value.text = """{"status": "success","email": "user@user.com","username": "useruser12345"}"""
        self.assertEqual(create_user("PASSword123_", "useruser12345", "user@user.com"),
        {
            "status": "success",
            "email": "user@user.com",
            "username": "useruser12345"
        })


if __name__ == '__main__':
    unittest.main()