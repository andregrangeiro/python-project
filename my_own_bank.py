# this is the main class of the program
class Account:
    def __init__(self, name, type, min_balance, balance):
        self.name = name
        self.type = type
        self.balance = balance
        self.min_balance = min_balance

# this is the method for depositing money into the customer's account
    def deposit(self, amount):
        self.balance += amount
        print()

# this is the method for withdrawing money from the customer's account
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(f"Here's ${amount}.")
            print()
        else:
            print("Sorry, not enough funds!")
            print()

# this is the method for showing the customer the current balance of his account.
    def statement(self):
        print(f"Account Balance ({self.type}): ${self.balance}")
        print()

# this class inherits from the "Account" class
class Current(Account):

    def __init__(self, name, type, balance=0, min_balance=-1000):
        super().__init__(name, type, balance, min_balance)

# this class inherits from the "Account" class
class Savings(Account):
    def __init__(self, name, type, balance=0, min_balance=0):
        super().__init__(name, type, balance, min_balance)

# greeting message
print("WELCOME TO GRAN BANK!")
print()

# asking for customer's name and assigning it to the "name" variable
name =  input("What is you name? ").capitalize()
print()

# asking for the account type the customer would like to open and  assigning it to the "account_type" variable
account_type = input(f"Hello, {name}. Which type of account would you like to open with us today?\nType 'c' for CURRENT or 's' for SAVINGS. ").strip().lower()
print()

# if the customer types "c", a current account object is instantiated and assigned to the "client_account" variable
if account_type == "c":
    account_type = "current"
    client_account = Current(name, account_type)

# else if the customer types "s", a savings account object is instantiated and assigned to the "client_account" variable
elif account_type == "s":
    account_type = "savings"
    client_account = Savings(name, account_type)

# asking the amount the customer would like to deposit and assigning it to the "first_deposit" variable
first_deposit = float(input(f"How much would you like to deposit in your new {account_type} account? "))
print()

# calling the "deposit" method with the "client_account" object
client_account.deposit(first_deposit)

# giving the customer feedback to make sure his deposit went through correctly
print(f"Thank you for your first deposit of ${first_deposit}, {name}.")
print()

# after the greeting message and the first deposit, this loop gives the customer options for services until he decides to exit
while True:
    option = int(input("What would you like to do next?\n\nType '1' to make a new deposit.\nType '2' to withdraw money.\nType '3' to check your account balance.\nType '4' to exit. "))
    print()

# asking for the amount the customer wants to deposit and assigning it to the "other_deposit" variable
# calling the "deposit" method with the "client_account" object | "other_deposit" is passed as an argument
    if option == 1:
        other_deposit = float(input(f"How much would you like to deposit in your {account_type} account today? "))
        client_account.deposit(other_deposit)
        print(f"Thank you for your deposit of {other_deposit}, {name}.")
        print()

# asking for the amount the customer wants to withdraw and assigning it to the "withdraw" variable
# calling the "withdraw" method with the "client_account" object | "withdraw" is passed as an argument
    elif option == 2:
        withdraw = float(input(f"How much would you like to withdraw, {name}? "))
        print()
        client_account.withdraw(withdraw)

# calling the "statement" method with the "client_account" object
    elif option == 3:
        client_account.statement()

# exiting the program when the customer chooses the option '4'
    elif option == 4:
        print("Thank you for your business with GRAN BANK. Come back soon!")
        break







