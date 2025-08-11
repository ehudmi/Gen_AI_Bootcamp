# What you will learn
# OOP
# Python Files I/O


# What you will create


# 🌟 Anagram checker
# We will create a program that will ask the user for a word.
# It will check if the word is a valid English word, and then find all possible anagrams for that word.


# Instructions
# First Download this text file

# Create a new file called anagram_checker.py which contains a class called AnagramChecker.

# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched
# later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is
# ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

# Hint: you might want to create a separate method called is_anagram(word1, word2), that will
# compare 2 words and return True if they contain the same letters (but not in the same order),
# and False if not.

# Note: None of the methods in the class should print anything.
from pathlib import Path
from itertools import permutations as permutations


class AnagramChecker:
    def __init__(self):
        self.word_list = []
        path_location = Path(__file__).parent / "sowpods.txt"
        with open(path_location, "r") as f:
            for line in f:
                self.word_list.append(line.strip())

    def is_valid_word(self, word):
        """check if the word is valid. i.e - in the list from file"""
        try:
            if word in self.word_list:
                return True
            else:
                return False
        except TypeError:
            return "The word provided is not a string"

    def get_anagrams(self, word: str):
        """check all combination of characters in word"""
        anagram_list = []
        word_split = list(word)
        try:
            for char_list in permutations(word_split):
                anagram = "".join(char_list)
                if self.is_valid_word(anagram):
                    anagram_list.append(anagram.lower())

        except TypeError:
            return "The word provided is not a string"
        return anagram_list
