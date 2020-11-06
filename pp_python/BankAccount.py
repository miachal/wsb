from AccountType import AccountType
from AccountException import AccountException
from AbstractAccount import AbstractAccount

class BankAccount(AbstractAccount):
  def __init__(self, id, balance = 0):
    self._id = id
    self._balance = balance
    self._type = AccountType.PL
    self._isActive = True

  def data(self):
    return [
      self._id,
      self._balance,
      self._type
    ]

  def isActive(self):
    return self._isActive

  def deposit(self, amount):
    self._balance += amount

  def withdraw(self, amount):
    if (self._balance < amount):
      raise AccountException('Lack of account funds.')
    self._balance -= amount

  def close(self):
    if self._isActive:
      self.withdraw(self._balance)
      self._isActive = False
    else:
      raise AccountException('This account is already closed.')

  def __repr__(self):
    return f'ID: {self._id}\tType: {self._type}\tBalance: {self._balance}\tActive: {"YES" if self._isActive else "NO"}'

