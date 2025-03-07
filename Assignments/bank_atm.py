""" Bank ATM program
"""
# print('Welcome to StillBank\nPlease choose an option\n1.Withdraw Cash\n2.Check Account Balance')

# user_accounts = {}
# pin = []

# account: int = input("Enter your account code:\n")
# user_accounts[account] = pin
# user_pin: int = input("Enter your new secret PIN:\n")
# confirm_pin: int = input("Enter PIN to confirm:\n")

# def user():
#     for number in user_accounts:
#         if number == account:
#             print("Account found")


# def create_pin(account, user_pin, confirm_pin, user_accounts):
#     if user_pin == confirm_pin:
#         pin.update(user_accounts[account])
#         print("PIN successfully created")
        
#     else:
#         print("PIN does not match. Try again")


    
class ATM:
    def __init__(self):
        # Dictionary to store user account information
        self.user_accounts = {}
        self.logged_in_user = None

    def create_account(self, account, user_pin):
        if account in self.user_accounts:
            print(f"Account {account} already exists.")
        else:
            # Initialize user account with a PIN and a starting balance of 0
            self.user_accounts[account] = {"pin": user_pin, "balance": 0}
            print(f"Account {account} successfully created.")

    def login(self, account, user_pin):
        # Check if the account exists and PIN matches
        if account in self.user_accounts and self.user_accounts[account]["pin"] == user_pin:
            self.logged_in_user = account
            print(f"Login successful for account {account}.")
        else:
            print("Invalid account or PIN. Please try again.")

    def logout(self):
        if self.logged_in_user:
            print(f"Logging out of account {self.logged_in_user}.")
            self.logged_in_user = None
        else:
            print("No user logged in.")

    def check_balance(self):
        if self.logged_in_user:
            print(f"Your balance is: ${self.user_accounts[self.logged_in_user]['balance']}")
        else:
            print("You need to log in first.")

    def deposit(self, amount):
        if self.logged_in_user:
            if amount > 0:
                self.user_accounts[self.logged_in_user]['balance'] += amount
                print(f"Deposited ${amount}. Your new balance is: ${self.user_accounts[self.logged_in_user]['balance']}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("You need to log in first.")


    def withdraw(self, amount):
        if self.logged_in_user:
            if amount > 0 and self.user_accounts[self.logged_in_user]['balance'] >= amount:
                self.user_accounts[self.logged_in_user]['balance'] -= amount
                print(f"Withdrew ${amount}. Your new balance is: ${self.user_accounts[self.logged_in_user]['balance']}")
            else:
                print("Insufficient funds.")
        else:
            print("You need to log in first.")

