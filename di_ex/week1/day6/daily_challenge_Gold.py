# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter
# some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt,
# and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

handle_type = ""
shift_chars = 0
while handle_type != "0" or handle_type != "1":
    handle_type = input("If you wish to encrypt enter 0 to decrypt enter 1\n")
    if handle_type == "0" or handle_type == "1":
        break
while True:
    try:
        shift_chars = int(input("What is the shift of chars?\n"))
        if int(shift_chars) in range(1, 27):
            break
    except ValueError as ve:
        print("Input a number between 1 and 26")

user_message = input("What is the message?\n")
if handle_type == "1":
    decoded_list = []
    user_message_list = user_message.split(" ")
    for word in user_message_list:
        decoded_word = ""
        for letter in word:
            decoded_word += chr(ord(letter) + shift_chars)
        decoded_list.append(decoded_word)
    print(f'The decoded message is:\n{" ".join(decoded_list)}')
else:
    coded_list = []
    user_message_list = user_message.split(" ")
    for word in user_message_list:
        coded_word = ""
        for letter in word:
            coded_word += chr(ord(letter) - shift_chars)
        coded_list.append(coded_word)
    print(f'The coded message is:\n{" ".join(coded_list)}')
