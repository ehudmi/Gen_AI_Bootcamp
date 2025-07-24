# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as
# D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:

# 18,22,24

# C = 50
# H = 30
# user_list = input("Please give me a list of numbers separated by commas\n").split(",")
# number_list = [int((int(i) * 2 * C / H) ** 0.5) for i in user_list]
# print(number_list)


# Exercise 2 : List of integers
# Instructions
# Given a list of 10 integers to analyze. For example:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]


# 1. Store the list of numbers in a variable.

# my_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2. Print the following information:
# a. The list of numbers – printed in a single line
# print(my_list)
# b. The list of numbers – sorted in descending order (largest to smallest)
# print(sorted(my_list, reverse=True))
# c. The sum of all the numbers
# print(sum(my_list))
# 3. A list containing the first and the last numbers.
# print([my_list[0], my_list[-1]])
# 4. A list of all the numbers greater than 50.
# print([i for i in my_list if i > 50])
# 5. A list of all the numbers smaller than 10.
# print([i for i in my_list if i < 10])
# 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# print([i**2 for i in my_list])
# 7. The numbers without any duplicates – also print how many numbers are in the new list.
# print(set(my_list), len(set(my_list)))
# 8. The average of all the numbers.
# print(sum(my_list) / len(my_list))
# 9. The largest number.
# print(max(my_list))
# 10.The smallest number.
# print(min(my_list))
# 11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
# sum = 0
# average = 0
# largest = 0
# smallest = 0
# for index, item in enumerate(my_list):
#     sum += item
#     average = sum / (index + 1)
#     if largest < item:
#         largest = item
#     if smallest > item:
#         smallest = item

# print(sum, average, largest, smallest)

# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100
# and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times.
# Each number should be added into a variable that you created earlier.

# user_list = []
# for i in range(1, 11):
#     try:
#         user_number = int(input("Please select a number between -100 and 100\n"))
#     except ValueError as ve:
#         print("That is not a number")
#     user_list.append(user_number)
# print(user_list)

# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself.
# Make sure that these random integers are between -100 and 100.

# import random as rnd

# my_list = [rnd.randint(-100, 100) for i in range(10)]
# print(my_list)

# 14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random!
# Generate a random positive integer no smaller than 50.

# my_list = [rnd.randint(-100, 100) for i in range(rnd.randint(1, 50))]
# print(my_list)

# 15. Bonus: Will the code work when the number of random numbers is not equal to 10?


# Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of
# our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

paragraph = (
    "The series originally focused on a World War II setting, with Infinity Ward developing "
    "Call of Duty (2003) and Call of Duty 2 (2005) and Treyarch developing Call of Duty 3 (2006). "
    "Infinity Ward's Call of Duty 4: Modern Warfare (2007) introduced a modern setting and proved to be "
    "the breakthrough title for the series, creating the Modern Warfare sub-series; a Modern Warfare "
    "remastered version was released in 2016. Two other entries, Modern Warfare 2 (2009) and "
    "Modern Warfare 3 (2011), were made. The sub-series received a reboot with Modern Warfare in 2019, "
    "Modern Warfare II in 2022, and Modern Warfare III in 2023. Infinity Ward has also developed two "
    "games outside of the Modern Warfare sub-series, Ghosts (2013) and Infinite Warfare (2016)"
)

# print(f"The paragraph contains {len(paragraph)} characters")
# print(f"The paragraph contains {paragraph.count('.')+paragraph.count(';')} sentences")
# cleaned_paragraph = "".join(
#     [char if char.isalpha() or char == " " else "" for char in paragraph]
# )
# cleaned_paragraph_1 = cleaned_paragraph.split(" ")
# paragraph_1 = [i for i in cleaned_paragraph_1 if i != ""]
# print(f"The paragraph contains {len(paragraph_1)} words")
# print(f"The paragraph contains {len(set(paragraph_1))} unique words")
# count_nb = 0
# for i in paragraph:
#     if not i.isspace():
#         count_nb += 1
# print(f"The paragraph contains {count_nb} non-whitespace characters")
# print(
#     f"The average amount of words per sentence is {len(paragraph_1)/(paragraph.count('.')+paragraph.count(';'))}"
# )
# print(f"The amount of non uniques words is {len(paragraph_1)-len(set(paragraph_1))}")

# Exercise 4 : Frequency Of The Words
# Instructions
# Write a program that prints the frequency of the words from the input.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1

user_string = (
    "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
)
string_list = user_string.split(" ")
for i in set(string_list):
    print(f"{i}:{string_list.count(i)}")
