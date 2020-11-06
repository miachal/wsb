from Bank import Bank
from AccountException import AccountException

bank = Bank()
bank.printAccounts()
print()
bank.load('test.csv')
bank.printAccounts()
print()

try:
  x = bank.getAccount('Julian')
except AccountException as e:
  print('Error:', e)

acc = bank.getAccount('INT_01')
print(acc)

acc.close()
print(acc)

bank.save('test2.csv')

print()
bank2 = Bank()
bank2.load('test2.csv')
bank2.printAccounts()