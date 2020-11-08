from AccountType import AccountType
from AccountException import AccountException
from AbstractAccount import AbstractAccount

class BankAccount(AbstractAccount):
  def __init__(self, id, balance = 0):
    self._id = id
    self._balance = balance
    self._type = AccountType.PL
    self._is_active = True

  def as_data(self):
    return [
      self._id,
      self._balance,
      self._type
    ]

  def is_active(self):
    return self._is_active

  def deposit(self, amount):
    self._balance += amount

  def withdraw(self, amount):
    if (self._balance < amount):
      raise AccountException('Lack of account funds.')
    self._balance -= amount

  def close(self):
    if self._is_active:
      self.withdraw(self._balance)
      self._is_active = False
    else:
      raise AccountException('This account is already closed.')

  def __eq__(self, account_id):
    return self._id == account_id

  def __str__(self):
    return f'ID: {self._id}\tType: {self._type}\tBalance: {self._balance}\tActive: {"YES" if self._is_active else "NO"}'

