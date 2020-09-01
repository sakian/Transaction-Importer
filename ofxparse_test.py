import codecs
import re
from ofxparse import OfxParser

# with codecs.open('C:/Users/mark.bremer/Downloads/accountactivity(1).qfx') as file:
with codecs.open('C:/Users/mark.bremer/Downloads/accountactivity.qfx') as file:
# with codecs.open('C:/Users/mark.bremer/Downloads/accountactivity(4).ofx') as file:
    ofx = OfxParser.parse(file)

print("ACCOUNT:")
account = ofx.account
print(account.account_id)           # The account number
print(account.account_type)                 # type (1=Debit, 2=Credit)
print(account.statement)            # A Statement object

print("\nSTATEMENT:")
statement = account.statement
print(statement.start_date)         # The start date of the transactions
print(statement.end_date)           # The end date of the transactions
print(statement.balance)            # The money in the account as of the statement date

print("\nTRANSACTIONS:")
for transaction in statement.transactions:
    print("{desc:<25}{date:<15}{amount:<15}{id}".format(
        desc=str(re.sub(' +', ' ', transaction.payee)),
        date=transaction.date.strftime('%Y-%m-%d'),
        amount=transaction.amount,
        id=transaction.id
    ))
