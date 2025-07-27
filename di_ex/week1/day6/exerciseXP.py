# 🌟 Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:

# Creating dictionaries
# Zip function or dictionary comprehension


# Instructions

# You are given two lists. Convert them into a dictionary where the first list contains the keys and
# the second list contains the corresponding values.


# Lists:

# keys = ["Ten", "Twenty", "Thirty"]
# values = [10, 20, 30]

# my_dict = {keys[i]: values[i] for i in range(3)}
# print(my_dict)

# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# 🌟 Exercise 2: Cinemax #2
# Key Python Topics:

# Looping through dictionaries
# Conditionals
# Calculations


# Instructions

# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


# Family Data:

# family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
# total_cost = 0
# for k, v in family.items():
#     if v >= 3 and v <= 12:
#         print(f"The ticket price for {k} is 10")
#         total_cost += 10
#     elif v > 12:
#         print(f"The ticket price for {k} is 15")
#         total_cost += 15
#     else:
#         print(f"The ticket price for {k} is 0")
# print(f"The total cost for the family is {total_cost}")


# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.


# Bonus:

# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

# family = {}
# total_cost = 0
# flag = True
# while flag:
#     name = input(f"What is the name of the family member we should add?\n")

#     try:
#         age = int(input(f"What is the age of the family member we added?\n"))
#         if age >= 3 and age <= 12:
#             print(f"The ticket price for {name} is 10")
#             total_cost += 10
#         elif age > 12:
#             print(f"The ticket price for {name} is 15")
#             total_cost += 15
#         else:
#             print(f"The ticket price for {name} is 0")
#         family.update({name: age})
#     except ValueError as ve:
#         print("You did not provide a correct age")

#     if input("would you like to continue? yes or no?\n").lower() == "yes":
#         continue
#     else:
#         flag = False
# print(f"The total cost for the family is {total_cost}")


# 🌟 Exercise 3: Zara
# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions

# Create and manipulate a dictionary that contains information about the Zara brand.


# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.

# brand["number_stores"] = 2

# Print a sentence describing Zara’s clients using the type_of_clothes key.

# print(
#     f'The Zara brand includes clothing of the types {" clothes, ".join(brand["type_of_clothes"])} clothes'
# )

# Add a new key country_creation with the value Spain.

# brand.update({"country_creation": "Spain"})

# Check if international_competitors exists and, if so, add “Desigual” to the list.

# if "international_competitors" in brand.keys():
#     brand["international_competitors"].append("Desigual")

# Delete the creation_date key.

# del brand["creation_date"]

# Print the last item in international_competitors.

# print(brand["international_competitors"][-1])

# Print the major colors in the US.

# print(brand["major_color"]["US"])

# Print the number of keys in the dictionary.

# print(len(brand.keys()))

# Print all keys of the dictionary.

# print(brand.keys())


# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this
# dictionary with the original brand dictionary and print the result.

# more_on_zara = {"creation_date": 1980, "number_stores": 1000}

# brand.update(more_on_zara)
# print(brand)

# 🌟 Exercise 4: Disney Characters
# Key Python Topics:

# Looping with indexes
# Dictionary creation
# Sorting


# Instructions

# You are given a list of Disney characters. Create three dictionaries based on different patterns as
# shown below:


# Character List:

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


# Expected Results:

# 1. Create a dictionary that maps characters to their indices:

# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# dict_1 = {item: index for index, item in enumerate(users)}

# 2. Create a dictionary that maps indices to characters:

# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# dict_1 = {index: item for index, item in enumerate(users)}

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:

# dict_1 = {item: index for index, item in enumerate(sorted(users))}

# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
