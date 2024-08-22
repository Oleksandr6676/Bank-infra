from pydantic import BaseModel, ConfigDict


class AccountCreate(BaseModel):
    owner: str
    initial_balance: float


class AccountResponse(BaseModel):
    id: int
    account_id: str
    owner: str
    balance: float

    model_config = ConfigDict(from_attributes=True)


class Transaction(BaseModel):
    amount: float
