# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

# my_fav_numbers = {3, 12, 36, 60, 120}
# my_fav_numbers.update([7, 144])
# print(my_fav_numbers)
# my_fav_numbers.discard(144)
# print(my_fav_numbers)
# friend_fav_numbers = {5, 9, 21, 45}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)


# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you
# can’t add more integers to a tuple.

# Tuples are immutable - you cannot change the tuple by adding items to it and you cannot change the items
# contained in them

# 🌟 Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear


# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")

# basket.remove("Blueberries")

# basket.insert(-1, "Kiwi")

# basket.insert(0, "Apples")

# basket.count("Apples")

# basket.clear()

# print(basket)

# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?

# a float is a non-integer number which means it includes a decimal point.
# an integer is a whole number with no decimal point precision

# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

# my_list = []
# for i in range(3, 11):
#     if i / 2 == int(i / 2):
#         my_list.append(int(i / 2))
#     else:
#         my_list.append(i / 2)
# print(my_list)

# 🌟 Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

# for i in range(1, 21):
#     print(i)

# for index, i in enumerate(range(1, 21)):
#     if index % 2 == 0:
#         print(i)

# 🌟 Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.

# my_name = "Ehud"
# not_same_name = True
# while not_same_name:
#     your_name = input("What is your name?\n")
#     if your_name == my_name:
#         not_same_name = False


# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

# favorite_fruits = input("enter your favorite fruits separated by spaces\n").split(" ")
# print(favorite_fruits)
# user_choice = input("Enter a fruit\n").lower()
# for index, i in enumerate(favorite_fruits):
#     if i.lower() == user_choice and index < len(favorite_fruits):
#         print("You chose one of your favorite fruits! Enjoy!")
#         break
#     elif index == len(favorite_fruits) - 1:
#         print("You chose a new fruit. I hope you enjoy it!")
#     else:
#         continue

# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

# toppings = []
# flag = False
# while not flag:
#     user_topping = input("Please enter a topping\n")
#     if user_topping == "quit":
#         flag = True
#     else:
#         toppings.append(user_topping)
#         print(f"Adding {user_topping} to your pizza.")
# pizza_price = 10 + len(toppings) * 2.5
# print(toppings)
# print(pizza_price)

# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

# total_cost = 0
# flag = True
# while flag:
#     try:
#         person_age = int(input("Enter age of family member\n"))
#         if person_age <= 0:
#             print("You have entered an impossible age")
#             continue
#         elif person_age < 3:
#             pass
#         elif person_age >= 3 and person_age <= 12:
#             total_cost += 10
#         else:
#             total_cost += 15
#     except ValueError as ve:
#         print("You should only enter numbers")

#     if input("would you like to continue? yes or no?\n").lower() == "yes":
#         continue
#     else:
#         flag = False
# print(total_cost)


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

# film_list = []
# flag = True
# while flag:
#     try:
#         person_name = input("What is your name\n")
#         person_age = int(input("Enter your age\n"))
#         if person_age <= 0:
#             print("You have entered an impossible age")
#             continue
#         elif person_age >= 16 and person_age <= 21:
#             film_list.append(person_name)
#         else:
#             pass
#     except ValueError as ve:
#         print("You should only enter numbers")

#     if input("would you like to continue? yes or no?\n").lower() == "yes":
#         continue
#     else:
#         flag = False
# print(film_list)

# 🌟 Exercise 10: Sandwich Orders
# Key Python Topics:

# Lists
# Loops (while)


# Instructions:

# Using the list:
# sandwich_orders = [
#     "Tuna",
#     "Pastrami",
#     "Avocado",
#     "Pastrami",
#     "Egg",
#     "Chicken",
#     "Pastrami",
# ]
# The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
# Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
# Print a message for each sandwich made, such as: "I made your Tuna sandwich."
# Print the final list of all finished sandwiches.

# finished_sandwiches = []
# counter = 0
# while counter < len(sandwich_orders):
#     if sandwich_orders[counter] == "Pastrami":
#         sandwich_orders.pop(counter)
#     else:
#         finished_sandwiches.append(sandwich_orders[counter])
#         print(f"I made your {sandwich_orders[counter]} sandwich")
#     counter += 1

# print(finished_sandwiches)
