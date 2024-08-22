import requests
from requests.auth import HTTPBasicAuth


def check_inn(inn_number):
    username = "emhbot"
    password = "emh-2024"

    url = "https://emehmon.uz/check-inn"

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "inn": inn_number
    }

    response = requests.post(url, headers=headers, auth=HTTPBasicAuth(username, password), json=data)

    if response.status_code == 200:
        response_data = response.json()
        check = response_data.get("check")
        return check



