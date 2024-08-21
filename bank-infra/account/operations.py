from typing import Dict, Optional
from .models import Account

accounts: Dict[int, Account] = {}
account_id_counter = 1

def create_account(account_number: str, owner: str) -> Account:
    global account_id_counter
    new_account = Account(
        id=account_id_counter,
        account_number=account_number,
        owner=owner,
    )
    accounts[account_id_counter] = new_account
    account_id_counter += 1
    return new_account

def get_account(account_id: int) -> Optional[Account]:
    return accounts.get(account_id)

def deposit(account_id: int, amount: float) -> Optional[Account]:
    account = get_account(account_id)
    if account:
        account.balance += amount
        return account
    return None

def withdraw(account_id: int, amount: float) -> Optional[Account]:
    account = get_account(account_id)
    if account and account.balance >= amount:
        account.balance -= amount
        return account
    return None
