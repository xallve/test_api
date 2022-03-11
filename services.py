import requests
import json
from constants import BASE_URL


class API:
    def __init__(self, password, username, email):
        self.password = password
        self.username = username
        self.email = email


    def create_user(self):
        user = {"password": self.password, "username": self.username, "email": self.email}
        r = requests.post(BASE_URL, data=user)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('ERROR: %s' % e)
        json_data = json.loads(r.text)
        return json_data