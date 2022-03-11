import unittest
from unittest.mock import Mock, patch
import json
import requests
from services import API
from constants import BASE_URL2


class APITest(unittest.TestCase):
    def test_api(self):
        r = requests.get(BASE_URL2)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)
        self.assertEqual(r.status_code, 200)


    @patch('services.requests.post')
    def test_create_user(self, mock_post):
        mgc = API("PASSword123_", "useruser12345", "user@user.com")
        mock_post.return_value.text = """{"status": "success", "email": "user@user.com", "username": "useruser12345"}"""
        self.assertEqual(mgc.create_user(),
        {
            "status": "success",
            "email": "user@user.com",
            "username": "useruser12345"
        })


if __name__ == '__main__':
    unittest.main()