from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.db_base import Base


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    memo = Column(String)
    date = Column(Date)
    amount = Column(Numeric(10, 2))
    fit_id = Column(String)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship("Account", back_populates="transactions")
