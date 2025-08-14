from anagram_checker import AnagramChecker


def play():
    while True:
        try:
            choice = int(input("Select an option:\n1. Input a word\n2. Exit\n"))
        except:
            print("Invalid input. Please enter 1 or 2.")
            continue
        if choice == 2:
            print("Bye!")
            break
        elif choice == 1:
            word = input("Please enter a word\n").strip().upper()
            if word.find(" ") > -1:
                print("You have input more than one word - please try again")
                continue
            if word.isalpha() == False:
                print("Your word contains non alphabetic characters - please try again")
                continue
            else:
                test_word = AnagramChecker()
                if test_word.is_valid_word(word) == False:
                    print("The word is not valid - not in our database")
                    continue
                else:
                    anagrams = test_word.get_anagrams(word)
                    print(
                        f'YOUR WORD : {word}\nthis is a valid English word.\nAnagrams for your word:{", ".join(anagrams)}'
                    )


play()

# Now create another Python file, called anagrams.py. This will contain all the UI (user interface)
# functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user
# chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and
# then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message.
# (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.
