import enum
from sqlalchemy import Column, Integer, String, Enum, Numeric, Date
from sqlalchemy.orm import relationship
from database.db_base import Base


class AccountType(enum.Enum):
    UNKNOWN = 0
    BANK = 1
    CREDIT_CARD = 2
    INVESTMENT = 3


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String)
    type = Column(Enum(AccountType))
    statement_balance = Column(Numeric(10, 2))
    statement_date = Column(Date)
    transactions = relationship("Transaction", back_populates="account")
