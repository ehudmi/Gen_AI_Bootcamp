# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.


# def insert_list(list, item, index) -> list:
#     """Insert an item at the index provided in the list provided"""
#     list.insert(index, item)
#     return list


# print(insert_list([1, 2, 3], 4, 2))


# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.


# def count_spaces(string) -> int:
#     """count spaces in a string"""
#     counter = string.count(" ")
#     return counter


# print(count_spaces("magic marker 2"))

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.


# def count_upper_lower(string):
#     """count num of upper and lower characters in string"""
#     count = [0, 0]
#     for i in string:
#         if i.isupper():
#             count[0] += 1
#         elif i.islower():
#             count[1] += 1
#         else:
#             continue
#     return count


# print(
#     f"The number of upper case characters in the string is {count_upper_lower('Welcome To The Class')[0]}\nThe number of lower case characters in the string is {count_upper_lower('Welcome To The Class')[1]}"
# )

# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

# >>>my_sum([1,5,4,2])
# >>>12


# def my_sum(list):
#     '''Find the sum of a list of numbers'''
#     sum = 0
#     for i in list:
#         sum += i
#     return sum


# print(my_sum([1, 5, 4, 2]))

# Exercise 5
# Instructions
# Write a function to find the max number in a list


# def find_max(list):
#     '''Find the highest number in a list of numbers'''
#     max = 0
#     for i in list:
#         if i > max:
#             max = i
#     return max


# print(find_max([0, 1, 3, 50]))

# >>>find_max([0,1,3,50])
# >>>50


# Exercise 6
# Instructions
# Write a function that returns factorial of a number


# def factorial(number):
#     '''return the factorial of a number'''
#     result = 1
#     for i in range(1, number + 1):
#         result *= i
#     return result


# print(factorial(4))


# >>>factorial(4)
# >>>24


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

# >>>list_count(['a','a','t','o'],'a')
# >>>2


# def list_count(list, item):
#     '''count the number of times an item appears in the list'''
#     counter = 0
#     for i in list:
#         if i == item:
#             counter += 1
#     return counter


# print(list_count(["a", "a", "t", "o"], "a"))

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

# >>>norm([1,2,2])
# >>>3


# def norm(list):
#     """return the L2-norm of a list"""
#     result = 0
#     for i in list:
#         result += i**2
#     return result**0.5


# print(norm([1, 2, 2]))

# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)


# def is_mono(list):
#     """find if list is monotonic"""
#     list_ascending = True

#     if len(list) <= 2:
#         return True

#     for i in range(1, len(list)):
#         if list[i] < list[i - 1]:
#             list_ascending = False
#             break
#     if list_ascending == True:
#         return list_ascending

#     list_descending = True
#     for i in range(1, len(list)):
#         if list[i] > list[i - 1]:
#             list_descending = False
#             break
#     return list_descending


# print(is_mono([2, 3, 3, 3]))


# >>>is_mono([7,6,5,5,2,0])
# >>>True

# >>>is_mono([2,3,3,3])
# >>>True

# >>>is_mono([1,2,0,4])
# >>>False


# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.


# def longest_word(list):
#     """find the longest word in a list"""
#     counter = 0
#     word = ""
#     for i in list:
#         if len(i) > counter:
#             counter = len(i)
#             word = i
#     return word


# print(longest_word(["the", "magic", "horse", "is", "wonderful", "but", "small"]))


# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in
# another one.


# def dif_list(list):
#     '''separate the strings and the integers in a list to two lists'''
#     integer_list = []
#     string_list = []
#     for i in list:
#         if type(i) == str:
#             string_list.append(i)
#         elif type(i) == int:
#             integer_list.append(i)
#     return string_list, integer_list


# print(dif_list(["number", -254, "is", "smaller", "than", 35, "or", 2]))

# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

# >>>is_palindrome('radar')
# >>>True

# >>>is_palindrome('John)
# >>>False


# def is_palindrome(string):
#     '''check if string is palindrome'''
#     for i in range(len(string)):
#         if string[i] != string[len(string) - 1 - i]:
#             return False
#     return True


# print(is_palindrome("John"))

# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:


# def sum_over_k(sentence, k):
#     """count all words with more characters than k"""
#     counter = 0
#     for word in sentence.split(" "):
#         if len(word) > k:
#             counter += 1
#     return counter


# print(sum_over_k("Do or do not there is no try", 2))


# >>>sentence = 'Do or do not there is no try'
# >>>k=2
# >>>sum_over_k(sentence,k)
# >>>3


# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):


# def dict_avg(dictionary):
#     '''return average of values in a dictionary'''
#     result = 0
#     for i in dictionary.values():
#         result += i
#     return result / len(dictionary.items())


# print(dict_avg({"a": 1, "b": 2, "c": 8, "d": 1}))

# >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
# >>>3


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:


# def common_div(num1, num2):
#     """find common divisors of 2 numbers"""
#     divisor_list = []
#     if num1 >= num2:
#         for i in range(2, num2 + 1):
#             if num1 % i == 0 and num2 % i == 0:
#                 divisor_list.append(i)
#     else:
#         for i in range(2, num1 + 1):
#             if num1 % i == 0 and num2 % i == 0:
#                 divisor_list.append(i)
#     return divisor_list


# print(common_div(10, 20))

# >>>common_div(10,20)
# >>>[2,5,10]


# Exercise 16
# Instructions
# Write a function that test if a number is prime:


# def is_prime(number):
#     """check if the number is a prime number"""
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True


# print(is_prime(11))

# >>>is_prime(11)
# >>>True


# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:


# def weird_print(list):
#     """print elements in list if value and index are even"""
#     print_list = []
#     for index, item in enumerate(list):
#         if index % 2 == 0 and item % 2 == 0:
#             print_list.append(item)
#     return print_list


# print(weird_print([1, 2, 2, 3, 4, 5]))

# >>>weird_print([1,2,2,3,4,5])
# >>>[2,4]


# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count
# of different types:


# def type_count(**kwargs):
#     """count types of arguments"""
#     type_dict = {}
#     for item in kwargs.values():
#         if type(item) not in type_dict.keys():
#             type_dict.setdefault(type(item), 1)
#         else:
#             type_dict[type(item)] += 1
#     return type_dict


# print(type_count(a=1, b="string", c=1.0, d=True, e=False))

# >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
# >>>int: 1, str:1 , float:1, bool:2


# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.

# By default the function uses whitespace but it should be able to take an argument for any character
# and split with that argument.


# def mim_split(string, splitter):
#     """mimic split function"""
#     string_list = []
#     index_counter = 0
#     for index, letter in enumerate(string):
#         if letter == splitter:
#             string_list.append(string[index_counter:index])
#             index_counter = index + 1
#     return string_list


# print(mim_split("a=1, b=string, c=1.0, d=True, e=False", ","))

# Exercise 20
# Instructions
# Convert a string into password format.


# def conv_string(string):
#     """convert a string into a password"""
#     password = ""
#     for i in string:
#         password += "*"
#     return password


# print(conv_string("mypassword"))

# Example:
# input : "mypassword"
# output: "***********"
