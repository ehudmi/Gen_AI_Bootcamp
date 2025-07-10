# 🌟 Exercise 1 : Functions Exercises #1
# Instructions
# Write the following functions

# difference

# this function takes in two parameters and returns the difference between the two
# difference(2,2) # 0
# difference(0,2) # -2


# def difference(a, b):
#     return a - b


# print(difference(0, 2))

# print_day

# this function takes in one parameter (a number from 1-7) and returns the day of the week
# (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7,
# the function should return None
# print_day(4) # "Wednesday"
# print_day(41) # None


# def print_day(num):
#     week_days = {
#         1: "Sunday",
#         2: "Monday",
#         3: "Tuesday",
#         4: "Wednesday",
#         5: "Thursday",
#         6: "Friday",
#         7: "Saturday",
#     }
#     if num in week_days.keys():
#         return week_days.get(num)
#     else:
#         return None


# print(print_day(4))

# last_element

# this function takes in one parameter (a list) and returns the last value in the list.
# It should return None if the list is empty.
# last_element([1,2,3,4]) # 4
# last_element([]) # None


# def last_element(a):
#     if type(a) != list:
#         return "You have to provide a list"
#     elif a == []:
#         return None
#     else:
#         return a[len(a) - 1]


# print(last_element([]))

# number_compare

# this function takes in two parameters (both numbers). If the first is greater than the second,
# this function returns “First is greater.” If the second number is greater than the first,
# the function returns “Second is greater.” Otherwise the function returns “Numbers are equal.”
# number_compare(1,1) # "Numbers are equal"
# number_compare(1,2) # "Second is greater"
# number_compare(2,1) # "First is greater"


# def number_compare(a, b):
#     def check_type():
#         if (type(a) == int or type(a) == float) and (
#             type(b) == int or type(b) == float
#         ):
#             return True
#         else:
#             return False

#     if check_type() == False:
#         return "One or both of the parameters is not a number"
#     elif a == b:
#         return "Numbers are equal"
#     elif a > b:
#         return "First is greater"
#     else:
#         return "Second is greater"


# print(number_compare(2.5, 1))


# single_letter_count

# this function takes in two parameters (two strings). The first parameter should be a word and
# the second should be a letter. The function returns the number of times that letter appears in
# the word. The function should be case insensitive (does not matter if the input is lowercase or
# uppercase). If the letter is not found in the word, the function should return 0.
# single_letter_count('amazing','A') # 2


# def single_letter_count(word, letter):
#     def check_parameter():
#         if type(word) != str or len(word) < 2:
#             return "The first parameter is not a string or not a word"
#         elif type(letter) != str or len(letter) != 1:
#             return "The second parameter is not a string or not a letter"
#         else:
#             pass

#     if check_parameter():
#         return check_parameter()
#     else:
#         return word.lower().count(letter.lower())


# print(single_letter_count("AntIcIpation", "i"))

# multiple_letter_count

# this function takes in one parameter (a string) and returns a dictionary with the keys
# being the letters and the values being the count of the letter.
# multiple_letter_count("hello") # {h:1, e: 1, l: 2, o:1}
# multiple_letter_count("person") # {p:1, e: 1, r: 1, s:1, o:1, n:1}


# def multiple_letter_count(word):
#     if type(word) != str:
#         return "The parameter is not a string"
#     else:
#         return {word[x]: word.count(word[x]) for x in range(len(word))}


# print(multiple_letter_count("person"))

# list_manipulation

# this function should take in three parameters (a list, command, location and value).

# If the command is “remove” and the location is “end”, the function should remove the last value in
# the list and return the value removed
# If the command is “remove” and the location is “beginning”, the function should remove the first
# value in the list and return the value removed
# If the command is “add” and the location is “beginning”, the function should add the value
# (fourth parameter) to the beginning of the list and return the list
# If the command is “add” and the location is “end”, the function should add the value
# (fourth parameter) to the end of the list and return the list
# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") # 1
# list_manipulation([1,2,3], "add", "beginning", 20) # [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) # [1,2,3,30]


# def list_manipulation(*args):
#     if "remove" in args and "end" in args:
#         return args[0].pop(-1)
#     elif "remove" in args and "beginning" in args:
#         return args[0].pop(0)
#     elif "add" in args and "beginning" in args:
#         args[0].insert(0, args[-1])
#         return args[0]
#     elif "add" in args and "end" in args:
#         args[0].insert(len(args[0]), args[-1])
#         return args[0]
#     else:
#         return "oops"


# print(list_manipulation([1, 2, 3], "add", "end", 30))

# is_palindrome

# A Palindrome is a word, phrase, number, or other sequence of characters which reads the same
# backward or forward. This function should take in one parameter and returns True or False
# depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and
# capitalization so that is_palindrome('a man a plan a canal Panama') returns True.
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False


# def is_palindrome(sequence):
#     def check_type():
#         if type(sequence) == str:
#             sequence_rev = sequence[::-1].replace(" ", "").lower()
#             return sequence_rev
#         elif type(sequence) == int:
#             sequence_rev = str(sequence)[::-1].lower()
#             return sequence_rev
#         else:
#             return "I don't know what to do"

#     if str(sequence).replace(" ", "").lower() == check_type():
#         return True
#     else:
#         return False


# print(is_palindrome(145541))


# frequency

# This function accepts a list and a search_term (this will always be a primitive value) and
# returns the number of times the search_term appears in the list.
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1


# def frequency(my_list, search_term):
#     return my_list.count(search_term)


# print(frequency([True, False, True, True], False))

# flip_case

# This function accepts a string and a letter and reverses the case of all occurances of the
# letter in the string.
# flip_case("Hardy har har", "h") # "hardy Har Har"


# def flip_case(string, letter):
#     new_string = list(string)
#     for i in range(len(string)):
#         if string[i].lower() == letter.lower():
#             new_string[i] = string[i].swapcase()

#     return "".join(new_string)


# print(flip_case("Hardy har har", "h"))


# multiply_even_numbers

# This function accepts a list of numbers and returns the product of all even numbers in the list.
# multiply_even_numbers([2,3,4,5,6]) # 48


# def multiply_even_numbers(my_list):
#     product = 1
#     for item in my_list:
#         if item % 2 == 0:
#             product *= item
#     return product


# print(multiply_even_numbers([2, 3, 4, 5, 6]))


# mode

# This function accepts a list of numbers and returns the most frequent number in the list of numbers.
# You can assume that the mode will be unique.
# mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4


# def mode(my_list):
#     values = list(set(my_list))
#     counter = 0
#     frequent = 0
#     for i in range(len(values)):
#         if counter < my_list.count(values[i]):
#             counter = my_list.count(values[i])
#             frequent = values[i]
#     return frequent


# print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))

# capitalize

# This function accepts a string and returns the same string with the first letter capitalized.
# capitalize("tim") # "Tim"
# capitalize("matt") # "Matt"


# def capitalize(string):
#     return string.capitalize()


# print(capitalize("tim"))

# compact

# This function accepts a list and returns a list of values that are truthy values.
# compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]


# def compact(test_list):
#     result = []
#     for item in test_list:
#         if bool(item) == True:
#             result.append(item)
#     return result


# print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))


# partition

# This function accepts a list and a callback function (which you can assume returns True or False).
# The function should iterate over each element in the list and invoke the callback function at each
# iteration. If the result of the callback function is True, the element should go into one list if
# it’s False, the element should go into another list. When it’s finished, partition should return
# both lists inside of one larger list.
# def is_even(num):
#     return num % 2 == 0

# partition([1,2,3,4], is_even) # [[2,4],[1,3]]


# def partition(my_list, is_even):
#     def is_even(num):
#         return num % 2 == 0

#     even_list = []
#     odd_list = []
#     for item in my_list:
#         if is_even(item):
#             even_list.append(item)
#         else:
#             odd_list.append(item)
#     return [even_list, odd_list]


# print(partition([1, 2, 3, 4], ()))


# intersection

# This function should accept a two dimensional list and return a list with the values that are
# the same in each list.
# intersection([1,2,3], [2,3,4]) # [2,3]


# def intersection(list_1, list_2):
#     return list(set(list_1) & set(list_2))


# print(intersection([1, 2, 3], [2, 3, 4]))

# once

# This function accepts a function and returns a new function that can only be invoked once.
# If the function is invoked more than once, it should return None. Hint you will need to define a
# new function inside of your once function and return that function. You can add properties to your
# inner function to see if it has run already.
# def add(a,b):
#     return a + b

# one_addition = once(add)

# one_addition(2,2) # 4
# one_addition(2,2) # undefined
# one_addition(12,200) # undefined


# def add(a, b):
#     return a + b


# def once(function):
#     run_once = False

#     def run_function(*args):
#         nonlocal run_once
#         if run_once:
#             return None
#         else:
#             run_once = True
#             return function(*args)

#     return run_function


# one_addition = once(add)
# print(one_addition(2, 2))
# print(one_addition(2, 2))
# print(one_addition(12, 200))


# Super bonus
# Research what decorators are and refactor your once code to use a decorator so that you can run

# @run_once
# def add(a,b):
#     return a + b

# add(2,2) # 4
# add(2,20) # None
# add(12,20) # None


# def once(function):
#     run_once = False

#     def run_function(*args):
#         nonlocal run_once
#         if run_once:
#             return None
#         else:
#             run_once = True
#             return function(*args)

#     return run_function


# @once
# def add(a, b):
#     return a + b


# print(add(2, 2))
# print(add(2, 2))
# print(add(12, 200))
