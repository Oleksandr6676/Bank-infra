from behave import given, when, then
import requests
from tests.helpers.helpers import create_account, get_account

BASE_URL = "http://localhost:5000/"


@given("Account is created and added to the database")
def step_impl(context):
    response = create_account(initial_balance=2000, owner="Greg")
    json_data = response.json()
    context.status_code = response.status_code
    context.id = json_data["id"]
    context.expected_balance = json_data["balance"]


@when('I call "{endpoint_name}" endpoint and store response')
def step_impl(context, endpoint_name):
    response = get_account(context.id)
    json_data = response.json()
    context.status_code = response.status_code
    context.received_id = json_data["id"]
    context.received_balance = json_data["balance"]




@then('I verify that response status code is equal to "{status_code}"')
def step_impl(context, status_code):
    assert context.status_code == int(status_code)



@then("I verify that response contains the correct account data")
def step_impl(context):
    assert context.id == context.received_id
    assert context.expected_balance == context.received_balance


