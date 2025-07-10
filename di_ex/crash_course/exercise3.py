# Instructions
# Write the following Python code to do the following (complete ALL of these using list comprehension).

# Given a list [1,2,3,4], print out all the values in the list.

# for item in [1, 2, 3, 4]:
#     print(item)

# print([item for item in range(1, 5)])

# Given a list [1,2,3,4], print out all the values in the list multiplied by 20.

# for item in [1, 2, 3, 4]:
#     print(item * 20)

# print([item * 20 for item in range(1, 5)])

# Given a list [“Elie”, “Tim”, “Matt”], return a new list with only the first letter ([“E”, “T”, “M”]).

# print(first_letter_list := [item[0] for item in ["Elie", "Tim", "Matt"]])

# Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).

# print(even_list := [item for item in range(1, 7) if item % 2 == 0])

# Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).

# print([item for item in [1, 2, 3, 4] if item in [3, 4, 5, 6]])

# Given a list of words [“Elie”, “Tim”, “Matt”] return a new list with each word reversed and in lower case ([‘eile’, ‘mit’, ‘ttam’]).

# print(reverse_list := [item[::-1].lower() for item in ["Elie", "Tim", "Matt"]])

# Given two strings “first” and “third”, return a new string with all the letters present in both words ([“i”, “r”, “t”]).

# print([item for item in "first" if item in "third"])

# For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).

# print(dozens_list := [item for item in range(1, 101) if item % 12 == 0])

# Given the string “amazing”, return a list with all the vowels removed ([‘m’, ‘z’, ‘n’, ‘g’]).

# print([item for item in "amazing" if item not in ["a", "e", "i", "o", "u"]])

# Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

# print(new_list := [[0, 1, 2] for item in range(1, 4)])

# Generate a list with the value:

# [
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]

# print(new_list := [[i for i in range(0, 10)] for x in range(0, 10)])
