import requests
import json
from constants import BASE_URL


def create_user(password, username, email):
    user = {"password": password, "username": username, "email": email}
    r = requests.post(BASE_URL, data=user)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    json_data = json.loads(r.text)
    return json_data