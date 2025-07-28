# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).

# car_list = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(",")
# print(f"There are {len(car_list)} companies in the list")
# print(sorted(car_list, reverse=True))

# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.

# letter_o = 0
# for i in car_list:
#     if i.index("o") >= 0:
#         letter_o += 1
# print(f'There are {letter_o} manufacturers with the letter "o"')


# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# letter_i = 0
# for i in car_list:
#     if i.find("i") < 0:
#         letter_i += 1
# print(f'There are {letter_i} manufacturers without the letter "i"')

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor",
# "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).

car_list = [
    "Honda",
    "Volkswagen",
    "Toyota",
    "Ford Motor",
    "Honda",
    "Chevrolet",
    "Toyota",
]

# car_list_unique = set(car_list)
# print(f'The companies with no duplicates are: {", ".join(car_list_unique)}')

# Print out the companies without duplicates, in a comma-separated string with no line-breaks
# (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies
# are now in the list.

# print(f"the list now contains {len(car_list_unique)} companies")

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of
# each manufacturer’s name.

# print(sorted([i[::-1] for i in car_list_unique]))
