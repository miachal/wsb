from Bank import Bank
from AccountException import AccountException

bank = Bank()
print(bank)
print()
bank.load('test.csv')
print(bank)
print()

try:
  bank['Julian']
except AccountException as e:
  print('Error:', e)

acc = bank['INT_01']
print(acc)

acc.close()
print(acc)

bank.save('test2.csv')

print()
bank2 = Bank()
bank2.load('test2.csv')
print(bank2)