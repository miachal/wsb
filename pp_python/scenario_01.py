from AccountException import AccountException
from Bank import Bank
from BankAccount import BankAccount
from BankAccount_INT import BankAccount_INT
from BankAccount_COVID19 import BankAccount_COVID19
from BankAccount_COVID19_company import BankAccount_COVID19_company

bank = Bank()
pl_01 = BankAccount('PL_01', 10000)
int_01 = BankAccount_INT('INT_01', 10000)
covid_01 = BankAccount_COVID19('COVID_01', 10000)
company_01 = BankAccount_COVID19_company('COMPANY_01', 10000)

for account in [pl_01, int_01, covid_01, company_01]:
  bank.add(account)
 
print(bank)

# BankAccount
print()
pl_01.deposit(200)
pl_01.withdraw(300)
print(pl_01)

try:
  pl_01.withdraw(50000)
except AccountException as e:
  print('Error:', e)

print()
print(pl_01)
pl_01.close()
try:
  pl_01.close()
except AccountException as e:
  print('Error: ', e)
print(pl_01)

# INT
print()
print(int_01)
int_01.withdraw(5000)
print(int_01)

# COVID
print()
print(covid_01)
try:
  covid_01.withdraw(2000)
except AccountException as e:
  print('Error:', e)


# COMPANY
print()
print(company_01)
company_01.deposit(1000)
company_01.deposit(1000)
try:
  company_01.close()
except AccountException as e:
  print('Error:', e)
print(company_01)

# CSV
print()
print(bank)
bank.save('test.csv')