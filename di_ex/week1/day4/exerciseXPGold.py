# Exercise 1: Concatenate lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

# list_1 = [
#     1,
#     2,
#     3,
#     4,
# ]
# list_2 = [7, 8, 9, 10]
# list_1.extend(list_2)
# print(list_1)


# Exercise 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

# for i in range(1500, 2501):
#     if i % 5 == 0 or i % 7 == 0:
#         print(i)

# Exercise 3: Check the index
# Instructions
# Using this variable

# names = ["Samus", "Cortana", "V", "Link", "Mario", "Cortana", "Samus"]
# Ask a user for their name, if their name is in the names list print out the index of the first
# occurrence of the name.

# Example: if input is 'Cortana' we should be printing the index 1

# user_name = input("What is your name?\n")

# if user_name in names:
#     print(names.index(user_name))
# else:
#     print("your name is not on the list")


# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.

# numbers_list = []
# for i in range(1, 4):
#     try:
#         user_number = int(input("Please input a number\n"))
#         numbers_list.append(user_number)
#     except ValueError as ve:
#         print("That is not a number")
# print(f"The greatest number is: {sorted(numbers_list)[-1]}")

# Test Data
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87

# The greatest number is: 87


# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a
# consonant.

# my_string = ""
# vowels = ["a", "e", "i", "o", "u"]
# for i in range(97, 123):
#     my_string = my_string + chr(i)
# for index, j in enumerate(my_string):
#     if j in vowels:
#         print(f"{my_string[index]} is a vowel")
#     else:
#         print(f"{my_string[index]} is a consonant")

# Exercise 6: Words and letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearance of the letter variable in
# each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and
# the letter.

# words = (input("Please insert 7 words separated by space\n")).split(" ")
# letter = input("Please input a letter\n")

# for item in words:
#     if letter in item:
#         print(
#             f"the letter {letter} was found at index position {item.index(letter)} in {item}"
#         )
#     else:
#         print(f"The letter {letter} was not found in {item}")

# Exercise 7: Min, Max, Sum
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your
# list actually starts at one and ends at one million. Use the sum() function to see how quickly
# Python can add a million numbers.

# my_list = [i for i in range(1, 1000001)]
# print(sum(my_list))
# print(min(my_list))
# print(max(my_list))


# Exercise 8 : List and Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple
# which contain every number.

# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# user_input = input("Please provide a sequence of comma-separated numbers\n").split(",")
# print(user_input)
# print(tuple(user_input))

# Exercise 9 : Random number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

# import random as rnd

# games_played = 0
# games_won = 0
# flag = True
# while flag:

#     rnd_number = rnd.randint(1, 9)
#     try:
#         user_number = int(input("Please select a number between 1 and 9\n"))
#         if user_number not in range(1, 10):
#             print("The number should be between 1 and 9")
#             continue
#     except ValueError as ve:
#         print("You should only enter numbers")
#         continue
#     if rnd_number == user_number:
#         games_won += 1
#         print("Winner")
#     else:
#         print("better luck next time")
#     games_played += 1
#     if input("would you like to continue? yes or no?\n").lower() == "yes":
#         continue
#     else:
#         flag = False

# print(f"You have played {games_played} games and won {games_won} games")
