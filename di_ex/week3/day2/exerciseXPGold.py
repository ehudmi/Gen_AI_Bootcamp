# Exercise 1: Bank Account
# Instructions
# Part I:

# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the
# int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception
# if not positive


class BankAccount:
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to make a deposit.")

        try:
            amount = float(amount)
        except ValueError:
            raise Exception("Deposit amount must be a number.")

        if amount <= 0:
            raise Exception("Deposit amount must be positive.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to make a withdrawal.")

        try:
            amount = float(amount)
        except ValueError:
            raise Exception("withdrawal amount must be a number.")

        if amount <= 0:
            raise Exception("withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("insufficient funds")

        self.balance -= amount
        return self.balance

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            return True
        else:
            self.authenticated = False
            return False


# Part II : Minimum balance account

# Create a MinimumBalanceAccount that inherits from BankAccount.
# Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
# Override the withdraw method so it only allows the user to withdraw money if the balance remains
# higher than the minimum_balance, raise an Exception if not.


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to make a withdrawal.")

        try:
            amount = float(amount)
        except ValueError:
            raise Exception("withdrawal amount must be a number.")

        if amount <= 0:
            raise Exception("withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(
                f"Withdrawal denied. Minimum balance of {self.minimum_balance} must be maintained."
            )


# Part III: Expand the bank account class

# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (False by default)

# Create a method called authenticate. This method should accept 2 strings : a username and a password.
#  If the username and password match the attributes username and password the method should set the
# authenticated boolean to True.

# Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action
# without being authenticated raise an Exception


# Part IV: BONUS Create an ATM class

# __init__:
# Accepts the following parameters: account_list and try_limit.

# Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
# Hint: isinstance()


class ATM:
    def __init__(self, account_list, try_limit):

        if not isinstance(account_list, list):
            raise Exception("Account list must be a list of accounts.")

        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                raise Exception(
                    "All items in account list must be a BankAccount or MinimumBalanceAccount instance."
                )
        self.account_list = account_list

        try:
            self.try_limit = int(try_limit)
            if self.try_limit <= 0:
                print("Invalid try limit. Setting to default of 2.")
                self.try_limit = 2
        except (ValueError, TypeError):
            print("Invalid try limit. Setting to default of 2.")
            self.try_limit = 2

        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):

        while True:
            try:
                choice = int(input("Select an option:\n1. Login\n2. Exit\n"))
            except:
                print("Invalid input. Please enter 1 or 2.")
                continue

            if choice == 2:
                print("Bye!")
                break
            elif choice == 1:
                if self.current_tries >= self.try_limit:
                    print(
                        "You have reached the maximum number of tries. Shutting down."
                    )
                    break

                current_username = input("What is your username?\n")
                current_password = input("What is your password?\n")
                account = self.login(current_username, current_password)

                if account:
                    self.current_tries = 0
                    self.show_account_menu(account)
                else:
                    self.current_tries += 1
                    print("You input an invalid username or password")
            else:
                print("Invalid choice. Please select 1 or 2.")

    def login(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                return account
        return None

    def show_account_menu(self, account):
        while True:
            print(f"Your current balance is {account.balance}")
            try:
                choice = int(
                    input("Select an option:\n1. Deposit\n2. Withdraw\n3. Exit\n")
                )
            except ValueError:
                print("Invalid input. Please enter 1, 2, or 3.")
                continue
            if choice == 3:
                account.authenticated = False
                print("Logging out and returning to main menu")
                return
            try:
                if choice == 1:
                    amount = input("pleas input the amount to deposit\n")
                    account.deposit(amount)
                    print(f"Deposit successful. Your new balance is {account.balance}")

                elif choice == 2:
                    amount = input("pleas input the amount to withdraw\n")
                    account.withdraw(amount)
                    print(
                        f"Withdrawal successful. Your new balance is {account.balance}"
                    )
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")
            except Exception as e:
                print(f"Transaction failed: {e}")


# Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then
# move along and set try_limit to 2.
# Hint: Check out this tutorial

# Sets attribute current_tries = 0

# Call the method show_main_menu (see below)

# Methods:
# show_main_menu:
# This method will start a while loop to display a menu letting a user select:
# Log in : Will ask for the users username and password and call the log_in method with the username
# and password (see below).
# Exit.

# log_in:
# Accepts a username and a password.

# Checks the username and the password against all accounts in account_list.
# If there is a match (ie. use the authenticate method), call the method show_account_menu.
# If there is no match with any existing accounts, increment the current tries by 1. Continue asking
# the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once
# reached display a message saying they reached max tries and shutdown the program.

# show_account_menu:
# Accepts an instance of BankAccount or MinimumBalanceAccount.
# The method will start a loop giving the user the option to deposit, withdraw or exit.


account1 = BankAccount(1000, "ehud", "magic1")
account2 = BankAccount(2000, "tova", "yoki")
account3 = BankAccount(5000, "hadas", "the_one")
account4 = BankAccount(1000, "ohad", "youtube")
account5 = MinimumBalanceAccount(100, "uri", "magic1", 100)

my_atm = ATM([account1, account2, account3, account4, account5], 3)
