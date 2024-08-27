import requests

BASE_URL = "http://localhost:5000/"

def create_account(initial_balance, owner):
    url = BASE_URL + "accounts/"
    data = {
    "initial_balance": initial_balance,
    "owner": owner
    }
    response = requests.post(url, json=data)
    return response


def get_account(account_id):
    url = f"{BASE_URL}accounts/{account_id}"
    response = requests.get(url)
    return response