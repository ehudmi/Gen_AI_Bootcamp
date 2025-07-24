# Instructions:
# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

# flag = True
# while flag:
#     try:
#         user_number = int(input("Please enter a number\n"))
#         user_length = int(input("Please enter length as a number\n"))
#         if user_length and user_length:
#             mult_list = [user_number * i for i in range(1, user_length + 1)]
#             print(mult_list)
#             flag = False
#         else:
#             continue
#     except ValueError as ve:
#         print("This is not a number")
#         continue


# Example 1:

# Input:

# number: 7
# length: 5
# Output:

# [7, 14, 21, 28, 35]


# Example 2:

# Input:

# number: 12
# length: 10
# Output:

# [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]


# Example 3:

# Input:
# number: 17
# length: 6
# Output:
# [17, 34, 51, 68, 85, 102]


# Challenge 2: Remove Consecutive Duplicate Letters


# Key Python Topics:
# input() function
# Strings and string manipulation
# Loops (for or while)
# Conditional statements (if)


# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

user_string = input("Please enter a string\n")
last_item = user_string[0]
new_string = last_item
for item in user_string:
    if item != last_item:
        new_string += item
    last_item = item

print(new_string)


# Example 1:

# Input:
# user’s word: "ppoeemm"
# Output:
# "poem"


# Example 2:

# Input:
# user’s word: "wiiiinnnnd"
# Output:
# "wind"


# Example 3:

# Input:
# user’s word: "ttiiitllleeee"
# Output:
# "title"


# Example 4:

# Input:
# user’s word: "cccccaaarrrbbonnnnn"
# Output:
# "carbon"


# Notes:
# The final string will not include any consecutive duplicates, but non-consecutive duplicates
# are
# allowed.
# Example: In "carbon", the two ‘r’s are allowed because they are not consecutive.
