import csv
from datetime import date
from AccountException import AccountException
from AccountType import AccountType
from BankAccount import BankAccount
from BankAccount_INT import BankAccount_INT
from BankAccount_COVID19 import BankAccount_COVID19
from BankAccount_COVID19_company import BankAccount_COVID19_company

class Bank:
  def __init__(self):
    self._accounts = []

  def add(self, account):
    self._accounts.append(account)

  def remove(self, account):
    self._accounts.remove(account)

  def _type_to_class(self, account_type):
    is_after_big_bang = str(date.today()) > '2020-04-01'
    return {
      str(AccountType.PL): BankAccount_COVID19 if is_after_big_bang else BankAccount,
      str(AccountType.INT): BankAccount_INT,
      str(AccountType.COMPANY): BankAccount_COVID19_company if is_after_big_bang else BankAccount
    }[account_type]

  def load(self, path):
    self._accounts = []
    with open(path) as csvfile:
      reader = csv.reader(csvfile, delimiter=';')
      for row in reader:
        account_id, balance, account_type = row
        account = self._type_to_class(account_type)
        self.add(account(account_id, int(balance)))

  def save(self, path):
    with open(path, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile,
        delimiter=';',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL,
      )
      for account in self._accounts:
        if account.isActive():
          writer.writerow(account.data())

  def printAccounts(self):
    header = f'{"-" * 30} BANK ACCOUNTS {"-" * 30}'
    print(header)
    for account in self._accounts:
      print(account)
    print('-' * len(header))

  def getAccount(self, account_id):
    try:
      acc = [account for account in self._accounts if account._id == account_id][0]
      return acc
    except IndexError:
      raise AccountException('Account with this name does not exists.')