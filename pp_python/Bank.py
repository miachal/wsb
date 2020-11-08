import csv
import textwrap
from os import linesep
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

  def _type_to_class(self, account_type):
    is_after_big_bang = date.today() > date(2020, 4, 1)
    return {
      str(AccountType.PL): BankAccount_COVID19 if is_after_big_bang else BankAccount,
      str(AccountType.INT): BankAccount_INT,
      str(AccountType.COMPANY): BankAccount_COVID19_company if is_after_big_bang else BankAccount
    }[account_type]

  def add(self, account):
    self._accounts.append(account)

  def remove(self, account):
    self._accounts.remove(account)

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
        if account.is_active():
          writer.writerow(account.as_data())

  def __str__(self):
    header = f'{"-" * 30} BANK ACCOUNTS {"-" * 30}'
    bottom = '-' * len(header)
    return linesep.join([
      header,
      linesep.join([str(account) for account in self._accounts]),
      bottom])

  def __getitem__(self, account_id):
    try:
      acc = [account for account in self._accounts if account == account_id][0]
      return acc
    except IndexError:
      raise AccountException('Account with this name does not exists.')