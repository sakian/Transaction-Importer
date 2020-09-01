import argparse
import re
from ofxparse import OfxParser
from database.base import Session, engine, Base
from database.account import Account, AccountType
from database.transaction import Transaction

# Script argument handling
parser = argparse.ArgumentParser()
parser.add_argument("ofx_file", help="The OFX file to be imported")
args = parser.parse_args()

# Get OFX content
with open(args.ofx_file) as file:
    ofx = OfxParser.parse(file)

# Init database stuff
Base.metadata.create_all(engine)
session = Session()

# Get account (create if it doesn't exist)
account = session.query(Account).filter_by(account_number=ofx.account.account_id).scalar()
if not account:
    account = Account(
        name="Test Account",
        account_number=ofx.account.account_id,
        type=AccountType(ofx.account.type),
        statement_balance=ofx.account.statement.balance,
        statement_date=ofx.account.statement.end_date
    )
    session.add(account)

# Build transaction list and add to account
new_transactions = []
for trx in ofx.account.statement.transactions:
    if not session.query(Transaction.id).filter_by(fit_id=trx.id).scalar():
        new_transactions.append(
            Transaction(
                memo=re.sub(' +', ' ', trx.payee),
                date=trx.date,
                amount=trx.amount,
                fit_id=trx.id
            )
        )
account.transactions.extend(new_transactions)
print("Added {} transactions".format(len(new_transactions)))

session.commit()
