# Instructions:
# 1. Ask for User Input:

user_string = input("Please give me a 10 character string\n")

# The string must be exactly 10 characters long.
# 2. Check the Length of the String:

if len(user_string) == 10:
    print("Perfect string")
    print(
        f"first character is {user_string[0]} and last character is {user_string[-1]}"
    )
elif len(user_string) < 10:
    print("String not long enough.")
else:
    print("String too long.")

# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 3. Print the First and Last Characters:

# Once the string is validated, print the first and last characters.
# 4. Build the String Character by Character:

# Using a for loop, construct and print the string character by character.
# Start with the first character, then the first two characters, and so on,
# until the entire string is printed.
# Hint: You can create a loop that goes through the string, adding one character at a time,
# and print it progressively.
new_string = ""
for i in user_string:
    new_string = new_string + i
    print(new_string)

# 5. Bonus: Jumble the String (Optional)

# As a bonus, try shuffling the characters in the string and print the newly jumbled string.
# Hint: You can use the random.shuffle function to shuffle a list of characters.

import random as rnd

user_string_list = list(user_string)
rnd.shuffle(user_string_list)
print("".join(user_string_list))
