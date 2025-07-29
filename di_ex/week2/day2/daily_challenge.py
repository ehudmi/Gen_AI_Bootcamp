# Instructions:

# You are given a “Matrix” string:


MATRIX_STR = """
7ii
Tsx
h%?
i #
sM 
$a 
#t%"""


# This represents a grid of characters, and your task is to decode the hidden message within.


# Understanding the Matrix:

# Imagine this string arranged in rows and columns, forming a grid.
# To work with it in Python, you’ll need to transform this string into a 2D list (a list of lists), where each inner list represents a row.


# Step 1: Transforming the String into a 2D List


def analyze_matrix(message):
    matrix = message.split("\n")
    if "" in matrix:
        matrix.remove("")
    for index, item in enumerate(matrix):
        matrix[index] = [i for i in item]
    return decode_matrix(handle_2d_list(matrix))


# Step 2: Processing Columns

# Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
# You’ll need to write code that iterates through the columns of your 2D list.
# Think about how you can access the elements of a 2D list by column.


def handle_2d_list(list_2d):
    matrix_decode = []

    for i in range(len(list_2d[0])):
        for j in range(len(list_2d)):
            matrix_decode.append(list_2d[j][i])
    return matrix_decode


# Step 3: Filtering Alpha Characters

# only select alpha characters (letters).
# For each character in a column, check if it’s an alpha character.
# If it is, add it to a temporary string.
# Think about how you can check if a character is an alphabet letter.


def decode_matrix(matrix_string):
    decoded_string = ""
    for letter in matrix_string:
        if letter.isalpha():
            decoded_string += letter
        else:
            decoded_string += " "
        if decoded_string[-2:] == "  ":
            decoded_string = decoded_string.replace("  ", " ").lstrip()
    return decoded_string


print(analyze_matrix(MATRIX_STR))
# Step 4: Replacing Symbols with Spaces

# Replace every group of symbols (non-alpha characters) between two alpha characters with a space.
# After you have gathered the alpha characters, you will need to iterate through them, and where there
# are non alpha characters between them, you will insert a space.
# Think about how you can keep track of when you encounter an alphabet character, and when you
# encounter a non alphabet character.


# Step 5: Constructing the Secret Message

# Combine the filtered and processed characters to form the decoded message.
# Print the decoded message.


# Example:


MATRIX_STR = """
7ii
Tsx
h%?
i #
sM 
$a 
#t%"""

# Step 1: Convert matrix_string to a 2D list (matrix)
matrix = []
# ... code to create matrix ...

# Step 2: Iterate through columns
# ... code to iterate through columns ...

# Step 3: Filter alpha characters
# ... code to filter alpha characters ...

# Step 4: Replace symbols with spaces
# decoded_message = ""
# ... code to replace symbols with spaces ...

# Step 5: Print the decoded message
# print(decoded_message)
