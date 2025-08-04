# 🌟 Exercise 3: Dogs Domesticated
# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.


# Key Python Topics:

# Inheritance
# super() function
# *args
# Random module


# Instructions:

# Step 1: Import the Dog Class

# In a new Python file, import the Dog class from the previous exercise.


# Step 2: Create the PetDog Class

# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “ all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the random tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.


# Step 3: Test PetDog Methods

# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.


# Example:

# # In a new file
# # import the Dog class

from exerciseXP import Dog
from random import choice as choice


class PetDog(Dog):
    def __init__(self, name, age, weight):
        # no need to put the details in the function, you are giving the solution</mark>
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        # no need to put the details in the function, you are giving the solution</>
        print(self.bark())
        self.trained = True

    def play(self, *args):
        play_string = self.name
        if len(args) == 0:
            play_string = f"{self.name} is playing alone"
        for index, item in enumerate(args):
            if index < len(args) - 1:
                play_string += f", {item}"
            else:
                play_string += f" and {item} all play together"
        return print(play_string)

        # ... code to print play message ...

    def do_a_trick(self):
        # no need to put the details in the function, you are giving the solution</mark>
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead",
            ]
            return print(f"{self.name} {choice(tricks)}")


# dog1 = PetDog()
# # Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play()
my_dog.play("Buddy")
my_dog.play("Buddy", "Max")
my_dog.play("Buddy", "Max", "Tim")
my_dog.do_a_trick()
