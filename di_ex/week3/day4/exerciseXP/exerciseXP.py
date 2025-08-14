# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Dunder methods (__str__, __int__, __repr__, __add__, __iadd__)
# Modules (importing and using)
# string module
# datetime module
# faker module


# 🌟 Exercise 1: Currencies
# Goal: Implement dunder methods for a Currency class to handle string representation, integer
# conversion, addition, and in-place addition.


# Key Python Topics:

# Dunder methods (__str__, __repr__, __int__, __add__, __iadd__)
# Type checking (isinstance())
# Raising exceptions (raise TypeError)


# Instructions:


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #     #Your code starts HERE
    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"

    def __repr__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"

    def __int__(self):
        if isinstance(self.amount, int):
            return self.amount
        else:
            return print("You have input a string and not a number")

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                result = self.amount + other.amount
                return result
            else:
                raise TypeError(
                    f"TypeError: Cannot add between Currency type {self.currency} and {other.currency}"
                )
        elif isinstance(other, int):
            result = self.amount + other
            return result
        else:
            raise TypeError(f"TypeError: the parameter provided is not a currency")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                result = self.amount + other.amount
                self.amount = result
                return self
            else:
                raise TypeError(
                    f"TypeError: Cannot add between Currency type {self.currency} and {other.currency}"
                )
        elif isinstance(other, int):
            result = self.amount + other
            self.amount = result
            return self
        else:
            raise TypeError(
                f"TypeError: the value you are trying to add is not a currency"
            )


# Using the code above, implement the relevant methods and dunder methods which will output the
# results below.

# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

# #the comment is the expected output
# print(c1)
# # '5 dollars'

# print(int(c1))
# # 5

# print(repr(c1))
# # '5 dollars'

# print(c1 + 5)
# # 10

# print(c1 + c2)
# # 15

# print(c1)
# # 5 dollars

# c1 += 5
# print(c1)
# # 10 dollars

# c1 += c2
# print(c1)
# # 20 dollars

# print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>


# 🌟 Exercise 2: Import
# Goal: Create a module with a function and import it into another file.


# Instructions:

# Create a func.py file with a function that sums two numbers and prints the result. Then, import
# and call the function from exercise_one.py.


# Key Python Topics:

# Modules (creating and importing)
# Functions


# Step 1: Create func.py

# Create a file named func.py.
# Define a function inside that file that takes two numbers as arguments, sums them, and prints the
# result.


# Step 2: Create exercise_one.py

# Create a file named exercise_one.py.
# Import the function from func.py using one of the import syntaxes provided in the instructions.
# Call the imported function with two numbers.


# 🌟 Exercise 3: String module
# Goal: Generate a random string of length 5 using the string module.


# Instructions:

# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase
# letters only.


# Key Python Topics:

# string module
# random module
# String concatenation


# Step 1: Import the string and random modules

# Import the string and random modules.
import string
import random

# Step 2: Create a string of all letters

# Read about the strings methods HERE to find the best methods for this step
my_str = string.ascii_letters

# Step 3: Generate a random string

# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.


def random_string(string):
    rand_str = ""
    for i in range(6):
        index = random.randint(0, len(string))
        char = string[index]
        rand_str += char
    return rand_str


print(random_string(my_str))

# 🌟 Exercise 4: Current Date
# Goal: Create a function that displays the current date.


# Key Python Topics:

# datetime module


# Instructions:

# Use the datetime module to create a function that displays the current date.

# Step 1: Import the datetime module

# Step 2: Get the current date

# Step 3: Display the date

import datetime

current_date = datetime.date.today()
print(current_date)


# 🌟 Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.


# Key Python Topics:

# datetime module
# Time difference calculations


# Instructions:

# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

# Step 2: Get the current date and time

# Step 3: Create a datetime object for January 1st of the next year

# Step 4: Calculate the time difference

# Step 5: Display the time difference

# import datetime

current_date = datetime.datetime.today()
fut_date = datetime.datetime(2026, 1, 1)
date_diff = fut_date - current_date
print(date_diff)

# 🌟 Exercise 6: Birthday and minutes
# Key Python Topics:

# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method


# Instructions:

# Create a function that accepts a birthdate as an argument (in the format of your choice), then
# displays a message stating how many minutes the user lived in his life.

# import datetime


def calculate_days(date):
    """calculate how many days lived"""
    birth_date = datetime.datetime(int(date[:4]), int(date[5:7]), int(date[8:]))
    current_date = datetime.datetime.today()
    date_diff = current_date - birth_date
    print(f"You have been alive for {int(date_diff.total_seconds())} seconds")


birthdate = input("Please enter a birthdate in YYYY/MM/DD format\n")
calculate_days(birthdate)


# 🌟 Exercise 7: Faker Module
# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
# Read more about this module HERE


# Key Python Topics:

# faker module
# Dictionaries
# Lists
# Loops


# Instructions:

# Install the faker module and use it to create a list of dictionaries, where each dictionary
# represents a user with fake data.

# Step 1: Install the faker module

# Step 2: Import the faker module

# Step 3: Create an empty list of users

# Step 4: Create a function to add users

# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
# Step 5: Call the function and print the users list

from faker import Faker

user_list = []
faker = Faker()


def gen_users(num_users):
    """function to generate users"""
    for i in range(num_users):
        new_user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code(),
        }
        user_list.append(new_user)
    return user_list


print(gen_users(6))
