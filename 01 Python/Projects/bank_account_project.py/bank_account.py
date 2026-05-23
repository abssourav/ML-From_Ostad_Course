class BankAccount:
    def __init__(self,initialAmount,accountName):
        self.balance = initialAmount
        self.name = accountName

        print(f"\nAccount '{self.name}' Created. \n Balance = {self.balance:.2f}")

    #Get Balance mathod
    def getBalance(self):
         print(f"\nAccount '{self.name}' . Balance = {self.balance:.2f}")
       
    #Deposite Here
    def deposite(self,amount):
        self.balance = self.balance + amount
        print("\nDeposite Completed. ",end='')
        self.getBalance()

