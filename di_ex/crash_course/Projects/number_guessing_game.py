from random import randint as r


def number_guessing_game():
    random_number = r(1, 100)
    max_attempts = 7
    counter = max_attempts
    for i in range(1, max_attempts + 1):
        user_guess = int(input(f"Please select an integer between 1 and 100\n"))
        if user_guess == random_number:
            print(f"Congratulations! Your guess is right. you guessed in {i} guesses")
            break
        elif user_guess < random_number:
            print(f"Too low! You have {max_attempts-i} guesses left")
            counter -= 1
        else:
            print(f"Too high! You have {max_attempts-i} guesses left")
            counter -= 1
    if counter == 0:
        print(f"Uou failed! The number chosen was {random_number}")


number_guessing_game()
