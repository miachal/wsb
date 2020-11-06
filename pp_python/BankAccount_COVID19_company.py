from AccountException import AccountException
from AccountType import AccountType
from BankAccount_COVID19 import BankAccount_COVID19

class BankAccount_COVID19_company(BankAccount_COVID19):
  def __init__(self, id, balance = 0):
    super().__init__(id, balance)
    self._supported = False
    self._type = AccountType.COMPANY

  def deposit(self, amount):
    if not self._supported:
      self._balance += 5000
      self._supported = True
    super().deposit(amount)
  
  def close(self):
    raise AccountException('This type of account cannot be closed.')