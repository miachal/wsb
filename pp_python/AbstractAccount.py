from abc import ABC, abstractmethod

class AbstractAccount(ABC):
  @abstractmethod
  def deposit(self, amount):
    pass

  @abstractmethod
  def withdraw(self, amount):
    pass

  @abstractmethod
  def close(self):
    pass