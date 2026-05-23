'''
Create a class BankAccount with a private attribute balance and provide methods deposit() and withdraw()
to modify the balance safely so that the balance cannot be accessed directly. Then create two subclasses 
SavingsAccount and CurrentAccount, each having a method account_type() that prints its respective account type. 
Demonstrate polymorphism by calling account_type() from different account objects.

'''


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,dep_amount):
        if dep_amount > 0:
            self.__balance += dep_amount
            print(f"Deposite successful.\nYour current balance is : {self.__balance}")
        else:
            print("Only accepted positive amount.")

    def withdraw(self,with_amount):
        if  self.__balance >= with_amount:
            self.__balance -= with_amount
            print(f"Withdraw successful.\nYour current balance is : {self.__balance}")
        else:
            print(f"Do not have sufficient amount to withdraw.\n Your balance is : {self.__balance}")
            
    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def account_type(self):
        print("Account type: savings account")

class CurrentAccount(BankAccount):
    def account_type(self):
        print("Account type: Current Account")

customer1 = BankAccount(10000)
customer1.deposit(50)
customer1.withdraw(5000)

# Demonstrate polymorphism from different account objects
accounts = [SavingsAccount(1000),CurrentAccount(5000)]
for account in accounts:
    account.account_type()