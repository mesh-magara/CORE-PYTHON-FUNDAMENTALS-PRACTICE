class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #add a method that displays the details of the person
    def details(self):
        names = self.name
        ages = self.age
        print(" ---- MY DETAILS ----  ")
        print(f"  NAME  :  {names}")
        print(f"  AGE   :   {ages}")

# Creating another class called bank account with deposit
class bank_account:
    def __init__(self,balance):
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited : {amount} and Balance : {self.__balance}")
    
    def withdraw(self,amount):
        
        if self.__balance < amount:
            print("You have insufficient funds in the account")
        else:
            self.__balance -= amount
            print(f"Withdrew : {amount} and Balance : {self.__balance}")
    
    def bank_balance(self):
        print(f"ACCOUNT BALANCE : {self.__balance}")

# Creating the instances of classes 
person1 = person("mary johnson", 24)
person1.details()

person2 = person("Jackson Hayes",30)
person2.details()

account1 = bank_account(100)
account2 = bank_account(0)
account3 = bank_account(2000)

account1.deposit(600)
account1.withdraw(200)
account1.bank_balance()

account2.deposit(1000)
account2.withdraw(3000)
account2.bank_balance()

account3.deposit(5000)
account3.withdraw(2000)
account3.bank_balance()