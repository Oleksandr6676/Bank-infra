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


class TransferRequest(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float


class TransferResponse(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float
    from_account_balance: float
    to_account_balance: float

    model_config = ConfigDict(from_attributes=True)
