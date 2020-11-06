from AccountException import AccountException
from BankAccount import BankAccount

class BankAccount_COVID19(BankAccount):
  def withdraw(self, amount):
    if (amount > 1000):
      raise AccountException('You can withdraw only 1000 today.')
    super().withdraw(amount)