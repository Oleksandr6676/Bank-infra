import uuid
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(
        String(36), unique=True, index=True, default=lambda: str(uuid.uuid4())
    )
    owner = Column(String(100), index=True)
    balance = Column(Float, default=0.0)
