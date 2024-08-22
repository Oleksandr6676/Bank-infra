from behave import given, when, then
import requests

base_url = BASE_URL = "http://localhost:5000/"

@given('Account is created and added to the database')
def step_impl(context):
    pass  # Placeholder for account creation

@when('I call "{endpoint_name}" endpoint and store response')
def step_impl(context, endpoint_name):
    pass  # Placeholder for calling the specified endpoint and storing the response

@then('I verify that response status code is equal to "{status_code}"')
def step_impl(context, status_code):
    pass  # Placeholder for verifying that the status code matches the expected status code

@then('I verify that response contains the correct account data')
def step_impl(context):
    pass  # Placeholder for verifying that the response contains the correct account data
