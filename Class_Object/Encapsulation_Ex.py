class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self, amount):
        self.__balance+=amount

    def withdraw(self, amount):
        if 0< amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Invalid Or Insufficient balance")
    
    def get_balance(self):
        return self.__balance

account=BankAccount("Prakash", 1000)
print(account.get_balance())

account.deposit(500)
print(account.get_balance())


account.withdraw(200)
print(account.get_balance())


    
        