# Exercise 1: Birthday Look-up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the
# dictionary, the key should be the person’s name, and the value should be their birthday.
# Tip : Use the format “YYYY/MM/DD”.

birthdays = {
    "Tova": "1962/11/21",
    "Ehud": "1966/12/03",
    "Hadas": "1995/09/18",
    "Ohad": "1997/06/23",
    "Uri": "2000/12/06",
}

# print(f"Hello user - You can look up the birthdays of the people in the list!")
# user_name = input("Give me a name so I can look it up\n")
# if user_name.capitalize() in birthdays.keys():
#     print(
#         f"The birthdate for {user_name.capitalize()} is {birthdays[user_name.capitalize()]}"
#     )

# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the
# people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.


# Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message
# (“Sorry, we don’t have the birthday information for <person’s name>”)

# print(birthdays)
# print(f"Hello user - You can look up the birthdays of the people in the list!")
# user_name = input("Give me a name so I can look it up\n")
# if user_name.capitalize() in birthdays.keys():
#     print(
#         f"The birthdate for {user_name.capitalize()} is {birthdays[user_name.capitalize()]}"
#     )
# else:
#     print(f"Sorry, we don’t have the birthday information for {user_name}")

# Exercise 3: Add Your Own Birthday
# Instructions
# Add this new code: before asking the user to input a person’s name to look up, ask the user to add
# a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that
# he entered himself – the corresponding birthday is found and displayed.

# print(birthdays)
# print(f"Hello user - You can look up the birthdays of the people in the list!")
# new_name = input("Give me a new name to add\n")
# new_birthday = input("What is that person's birthdate in YYYY\MM\DD format?\n")
# if new_name.capitalize() not in birthdays.keys():
#     birthdays.update({new_name.capitalize(): new_birthday})
# else:
#     print(f"{new_name.capitalize()} is already in the list")
# user_name = input("Give me a name so I can look it up\n")
# if user_name.capitalize() in birthdays.keys():
#     print(
#         f"The birthdate for {user_name.capitalize()} is {birthdays[user_name.capitalize()]}"
#     )
# else:
#     print(f"Sorry, we don’t have the birthday information for {user_name}")


# Exercise 4: Fruit Shop
# Instructions
# items = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
# Using the dictionary above, each key-value pair represents an item and its price - print all the
# items and their prices in a sentence.

# phrase = []
# for k, v in items.items():
#     if k[0] in ["a", "e", "i", "o", "u"]:
#         phrase.append(f"an {k} costs {v}")
#     else:
#         phrase.append(f"a {k} costs {v}")
# print(f'Here are the items and their prices: {", ".join(phrase)}')

# Using the dictionary below, each value are dictionaries containing both the price and the amount
# of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1},
}

# total_cost = 0
# for fruit, details in items.items():
#     item_cost = details["price"] * details["stock"]
#     total_cost += item_cost
# print(total_cost)
