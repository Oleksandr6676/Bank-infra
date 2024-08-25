from behave import given, when, then
import requests

BASE_URL = "http://localhost:5000/"


@given("Account is created and added to the database")
def step_impl(context):
    url = BASE_URL + "accounts/"
    data ={
        "initial_balance": 2000,
        "owner": "Greg"
    }
    response = requests.post(url, json=data)
    json_data = response.json()
    context.status_code = response.status_code
    context.id = json_data["id"]
    context.balance = json_data["balance"]


@when('I call "{endpoint_name}" endpoint and store response')
def step_impl(context, endpoint_name):
    url = f"{BASE_URL}accounts/{context.id}"
    response = requests.get(url)
    json_data = response.json()
    context.status_code = response.status_code
    context.received_id = json_data["id"]
    context.received_balance = json_data["balance"]




@then('I verify that response status code is equal to "{status_code}"')
def step_impl(context, status_code):
    assert context.status_code == 200



@then("I verify that response contains the correct account data")
def step_impl(context):
    assert context.id == context.received_id
    assert context.balance == context.received_balance


