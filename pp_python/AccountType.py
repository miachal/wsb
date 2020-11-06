from enum import Enum

class AccountType(Enum):
  PL = 1
  INT = 2
  COMPANY = 3

  def __str__(self):
    return self.name