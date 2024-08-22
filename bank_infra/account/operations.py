from sqlalchemy.orm import Session
import uuid
from bank_infra.account import models, schemas


def create_account(db: Session, account: schemas.AccountCreate):
    db_account = models.Account(
        account_id=str(uuid.uuid4()),
        owner=account.owner,
        balance=account.initial_balance,
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()


def deposit(db: Session, account_id: int, amount: float):
    account = get_account(db, account_id)
    if account:
        account.balance += amount
        db.commit()
        db.refresh(account)
        return account
    return None


def withdraw(db: Session, account_id: int, amount: float):
    account = get_account(db, account_id)
    if account and account.balance >= amount:
        account.balance -= amount
        db.commit()
        db.refresh(account)
        return account
    return None
