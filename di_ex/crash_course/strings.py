# Exercise 1

# We’ll use a string and apply several string methods to see how they change the text. Follow the steps below, run the code, and observe the results!

# text = "Python is Fun!"
# 1. Convert the entire string to uppercase

# print(text.upper())

# 2. Make the first letter upper case

# print(text.capitalize())

# 3. Make the first letter of each word upper case

# print(text.title())

# 4. Find the index of "F". What happens if you use lower case in the method?

# print(text.index("F"))

# 5. Find a substring

# print(text.find("is"))

# Exercise 2

# Write a Python program that:

# 1. Asks the user to input a sentence.

# 2. Checks if the sentence is made up of only alphabetic characters. If not, print how many non-alphabetic characters are in the sentence.

# 3. Determines if the sentence ends with an exclamation mark (!).

# 4. Finds out if the sentence contains any whitespace characters and prints a message accordingly.

user_sentence = input("Please insert a sentence\n")
if user_sentence.isalpha():
    print("Your sentence contains only alphabetic characters")
else:
    count = 0
    for i in range(len(user_sentence)):
        if user_sentence[i].isspace():
            count += 1
    print(f"Your sentence contains {count} non-alphabet characters")
if user_sentence.endswith("!"):
    print("Your sentence ends with an exclamation mark")
if user_sentence.find(" ") != 0:
    print("your sentence contains whitespace characters")
