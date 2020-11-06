from AccountType import AccountType
from BankAccount import BankAccount

class BankAccount_INT(BankAccount):
  def __init__(self, id, balance = 0):
    super().__init__(id, balance)
    self._type = AccountType.INT
    