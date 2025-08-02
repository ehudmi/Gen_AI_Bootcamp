# Instructions
# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a
# target number.

# import random

# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

# target_number = 3728


# def check_sum(list, target):
#     """Check if the sum reaches the target"""
#     short_list = [i for i in list if i <= target]
#     sum_list = []
#     for i in short_list:
#         if target - i in short_list:
#             sum_list.append((i, target - i))
#     return sum_list


# print(check_sum(list_of_numbers, target_number))


# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that
# sum to the target number

# For example

# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728
