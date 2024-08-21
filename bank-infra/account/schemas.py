from pydantic import BaseModel

class AccountCreate(BaseModel):
    account_number: str
    owner: str

class AccountResponse(BaseModel):
    id: int
    account_number: str
    owner: str
    balance: float

class Transaction(BaseModel):
    amount: float