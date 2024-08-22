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


def delete_account(db: Session, account_id: int):
    db_account = get_account(db, account_id)
    if db_account:
        db.delete(db_account)
        db.commit()
        return True
    return None


def transfer(db: Session, from_account_id: int, to_account_id: int, amount: float):
    from_account = get_account(db, from_account_id)
    to_account = get_account(db, to_account_id)

    if from_account and to_account and from_account.balance >= amount:
        from_account.balance -= amount
        to_account.balance += amount
        db.commit()
        db.refresh(from_account)
        db.refresh(to_account)
        return {
            "from_account_id": from_account_id,
            "to_account_id": to_account_id,
            "amount": amount,
            "from_account_balance": from_account.balance,
            "to_account_balance": to_account.balance,
        }
    return None


def get_all_accounts(db: Session):
    return db.query(models.Account).all()
