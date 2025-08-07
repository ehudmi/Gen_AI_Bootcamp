# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions
# of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm,
# right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or
# all six body parts are on the gallows.
# The player can’t guess the same letter twice.


# Starter code
# Here is a piece of code that will give you a random word.

import random

wordslist = [
    "correction",
    "childish",
    "beach",
    "python",
    "assertive",
    "interference",
    "complete",
    "share",
    "credit card",
    "rush",
    "south",
]
word = random.choice(wordslist)

#     ### YOUR CODE STARTS FROM HERE ###
print("Welcome to hangman")

word_hidden = ["*" for i in range(len(word))]
hangman_parts = ["O", "|", "/", "\\", "/ ", "\\"]


def draw_hangman(num_parts):
    """Draw the hangman with the number parts supplied"""
    hangman = f"""{'-'*6}\n|{' '*4}|\n"""
    if num_parts == 1:
        hangman += f"|{' '*4}{hangman_parts[0]}\n|\n|\n"
        return hangman
    elif num_parts == 2:
        hangman += f"|{' '*4}{hangman_parts[0]}\n|{' '*4}{hangman_parts[1]}\n|\n"
        return hangman
    elif num_parts == 3:
        hangman += f"|{' '*4}{hangman_parts[0]}\n|{' '*3}{hangman_parts[2]}{hangman_parts[1]}\n|\n"
        return hangman
    elif num_parts == 4:
        hangman += f"|{' '*4}{hangman_parts[0]}\n|{' '*3}{hangman_parts[2]}{hangman_parts[1]}{hangman_parts[3]}\n|\n"
        return hangman
    elif num_parts == 5:
        hangman += f"|{' '*4}{hangman_parts[0]}\n|{' '*3}{hangman_parts[2]}{hangman_parts[1]}{hangman_parts[3]}\n|{' '*3}{hangman_parts[4]}"
        return hangman
    elif num_parts == 6:
        hangman += f"|{' '*4}{hangman_parts[0]}\n|{' '*3}{hangman_parts[2]}{hangman_parts[1]}{hangman_parts[3]}\n|{' '*3}{hangman_parts[4]}{hangman_parts[5]}\n"
        return hangman


print(draw_hangman(6))


def input_guess(letter, word_hidden, counter):
    """Checking the player's guess"""
    word_drawing = ""
    print(word)
    for index, item in enumerate(word):
        if item == letter:
            word_hidden[index] = letter
            word_drawing = "".join(word_hidden)
            return word_drawing, counter
    if word_drawing == "":
        counter = counter + 1
        return word_drawing, counter


def play():
    counter = 0
    while True:
        result = input_guess(
            input("Please select a letter a-z\n").lower(), word_hidden, counter
        )
        print(result)
        if result[1] < 6:
            print(draw_hangman(result[1]))
        if result[1] == 6:
            print(draw_hangman(result[1]))
            print("Sorry! You lost")
            break
        if result[0] == word:
            print("Congrats! You won")
            break


play()
