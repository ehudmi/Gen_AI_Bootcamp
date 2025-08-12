# Exercise 1 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday
# and print which holiday that is. (Example: the next holiday is New Years’ Eve in 30 days).
# Hint: Use a module to find the datetime and name of the upcoming holiday.

# from datetime import date as date
# from holidays import country_holidays as holidays


# def find_holiday():
#     isr_holiday = holidays("ISR")
#     current_date = date.today()
#     next_holiday = isr_holiday.get_closest_holiday()
#     date_diff = next_holiday[0] - current_date
#     return f"Today is {current_date}. the next holiday is {next_holiday[1]} in {date_diff.days} days"


# try:
#     print(find_holiday())
# except Exception as e:
#     print("something went boom")


# Exercise 2 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on all those planets :

# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Example : if someone is 1,000,000,000 seconds old, the function should output that they are 31.69
# Earth-years old.
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years

# ORBITAL_YEARS = {
#     "Earth": {"earth_years": 1, "seconds": 31557600},
#     "Mercury": {"earth_years": 0.2408467},
#     "Venus": {"earth_years": 0.61519726},
#     "Mars": {"earth_years": 1.8808158},
#     "Jupiter": {"earth_years": 11.862615},
#     "Saturn": {"earth_years": 29.447498},
#     "Uranus": {"earth_years": 84.016846},
#     "Neptune": {"earth_years": 164.79132},
# }


# def calc_age(seconds):
#     for planet, data in ORBITAL_YEARS.items():
#         planet_age = seconds / (ORBITAL_YEARS["Earth"]["seconds"] * data["earth_years"])
#         print(f"Your age on planet {planet} is {planet_age:.2f} years")


# try:
#     user_age_in_seconds = int(input("Please enter your age in seconds: "))
#     calc_age(user_age_in_seconds)
# except ValueError:
#     print("Invalid input. Please enter a whole number.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

# Exercise 3 : Regular Expression #1
# Instructions
# Hint: Use the RegEx (module)

# Use the regular expression module to extract numbers from a string.

# Example

# return_numbers('k5k3q2g5z6x9bn')
# // Excepted output : 532569
# import re


# def return_numbers(string: str):
#     """extract digits from string"""
#     pattern = re.compile(r"[0-9]")
#     print("".join(pattern.findall(string)))


# return_numbers("k5k3q2g5z6x9bn")


# Exercise 4 : Regular Expression #2
# Instructions
# Hint: Use the RegEx (module)

# Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
# The name should contain only letters.
# The name should contain only one space.
# The first letter of each name should be upper cased.

# import re


# def user_info(name):
#     pattern = re.compile(r"^[A-Z][a-z]*\s[A-Z][a-z]*")
#     if pattern.fullmatch(name):
#         print(f"Your name {name} checks out")
#     else:
#         print("Try again")


# try:
#     your_name = input(
#         "What is your name - capitalize first name and family name please\n"
#     )
#     user_info(your_name)
# except:
#     print("you made a booboo")

# Exercise 5: Python Password Generator
# Instructions
# Create a Python program that will generate a good password for you.

# Program flow:

# Ask the user to type in the number of characters that the password should have (password length) –
# between 6 and 30 characters.
# Validate the input. Make sure the user is inputing a number between 6 to 30. Create a loop which
# will continue to ask the user for an input until they enter a valid one.

# Generate a password with the required length.

# Print the password with a user-friendly message which reminds the user to keep the password in a
# safe place!

# Rules for the validity of the password

# Each password should contain:
# At least 1 digit (0-9)
# At least 1 lower-case character (a-z)
# At least 1 upper-case character (A-Z)
# At least 1 special character (eg. !, @, #, $, %, ^, _, …)
# Once there is at least 1 of each, the rest of the password should be composed of more characters
# from the options presented above.

# Create a test function first!

# Do the following steps 100 times, with different password lengths:
# Generate a password.
# Test the password to ensure that:
# it fulfills all the requirements above (eg. it has at least one digit, etc.)
# it has the specified length.
import re
from random import randint, choices


def password_generator(start, end):
    password = ""
    length = end - start
    for _ in range(start, end + 1):
        password
