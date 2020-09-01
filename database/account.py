import enum
from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy.orm import relationship
from database.base import Base
from database.currency_type import Currency


class AccountType(enum.Enum):
    UNKNOWN = 0
    BANK = 1
    CREDIT_CARD = 2
    INVESTMENT = 3


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    account_number = Column(String)
    type = Column(Enum(AccountType))
    statement_balance = Column(Currency)
    statement_date = Column(Date)
    transactions = relationship("Transaction", back_populates="account")
