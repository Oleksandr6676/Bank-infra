from fastapi import FastAPI, HTTPException
from account import operations, schemas

app = FastAPI()

@app.post("/accounts/", response_model=schemas.AccountResponse)
def create_account(account: schemas.AccountCreate):
    new_account = operations.create_account(account_number=account.account_number, owner=account.owner)
    return new_account

@app.get("/accounts/{account_id}", response_model=schemas.AccountResponse)
def read_account(account_id: int):
    account = operations.get_account(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@app.post("/accounts/{account_id}/deposit/", response_model=schemas.AccountResponse)
def deposit_money(account_id: int, transaction: schemas.Transaction):
    account = operations.deposit(account_id, amount=transaction.amount)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@app.post("/accounts/{account_id}/withdraw/", response_model=schemas.AccountResponse)
def withdraw_money(account_id: int, transaction: schemas.Transaction):
    account = operations.withdraw(account_id, amount=transaction.amount)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found or insufficient balance")
    return account
