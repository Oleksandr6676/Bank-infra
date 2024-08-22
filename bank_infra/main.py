from flask import Flask, jsonify, request, abort
from flasgger import Swagger
from bank_infra.account import models, schemas, operations
from bank_infra.database.db import engine, get_db

app = Flask(__name__)

models.Base.metadata.create_all(bind=engine)

@app.route("/accounts/", methods=["POST"])
def create_account():
    """
    Create a new account
    ---
    tags:
      - Accounts
    parameters:
      - in: body
        name: body
        description: Account to be created
        schema:
          $ref: '#/definitions/AccountCreate'
    responses:
      200:
        description: The account was created
        schema:
          $ref: '#/definitions/AccountResponse'
    """
    db = next(get_db())
    account_data = request.json
    account_schema = schemas.AccountCreate(**account_data)
    account = operations.create_account(db=db, account=account_schema)
    return jsonify(schemas.AccountResponse.model_validate(account).model_dump())

@app.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    """
    Get details of a specific account
    ---
    tags:
      - Accounts
    parameters:
      - in: path
        name: account_id
        type: integer
        required: true
        description: The ID of the account
    responses:
      200:
        description: Account details
        schema:
          $ref: '#/definitions/AccountResponse'
      404:
        description: Account not found
    """
    db = next(get_db())
    db_account = operations.get_account(db, account_id=account_id)
    if not db_account:
        abort(404, description="Account not found")
    return jsonify(schemas.AccountResponse.model_validate(db_account).model_dump())

@app.route("/accounts/<int:account_id>/deposit/", methods=["POST"])
def deposit_money(account_id):
    """
    Deposit money into an account
    ---
    tags:
      - Accounts
    parameters:
      - in: path
        name: account_id
        type: integer
        required: true
        description: The ID of the account
      - in: body
        name: body
        description: Transaction details
        schema:
          $ref: '#/definitions/Transaction'
    responses:
      200:
        description: Account updated with the deposited amount
        schema:
          $ref: '#/definitions/AccountResponse'
      404:
        description: Account not found
    """
    db = next(get_db())
    transaction_data = request.json
    transaction_schema = schemas.Transaction(**transaction_data)
    account = operations.deposit(db, account_id=account_id, amount=transaction_schema.amount)
    if not account:
        abort(404, description="Account not found")
    return jsonify(schemas.AccountResponse.model_validate(account).model_dump())

@app.route("/accounts/<int:account_id>/withdraw/", methods=["POST"])
def withdraw_money(account_id):
    """
    Withdraw money from an account
    ---
    tags:
      - Accounts
    parameters:
      - in: path
        name: account_id
        type: integer
        required: true
        description: The ID of the account
      - in: body
        name: body
        description: Transaction details
        schema:
          $ref: '#/definitions/Transaction'
    responses:
      200:
        description: Account updated after withdrawal
        schema:
          $ref: '#/definitions/AccountResponse'
      404:
        description: Account not found or insufficient balance
    """
    db = next(get_db())
    transaction_data = request.json
    transaction_schema = schemas.Transaction(**transaction_data)
    account = operations.withdraw(db, account_id=account_id, amount=transaction_schema.amount)
    if not account:
        abort(404, description="Account not found or insufficient balance")
    return jsonify(schemas.AccountResponse.model_validate(account).model_dump())

definitions = {
    "AccountCreate": schemas.AccountCreate.model_json_schema(),
    "AccountResponse": schemas.AccountResponse.model_json_schema(),
    "Transaction": schemas.Transaction.model_json_schema(),
}
app.config['SWAGGER'] = {
    'title': 'Bank API',
    'uiversion': 3
}
swagger = Swagger(app, template={'definitions': definitions})

if __name__ == "__main__":
    app.run(debug=True)
