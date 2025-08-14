from pathlib import Path
import string
import re


class Text:
    def __init__(self, text: str):
        # initialize with text
        self.text = text
        self.word_list = self.text.split()

    def word_frequency(self, word):
        # split the text into list of words and count occurrences of word
        if word in self.word_list:
            return self.word_list.count(word)
        else:
            return f"the word {word} does not appear in the text"

    def most_common_word(self):
        # create dictionary of word occurrences and return list of most common words
        occurrences = {word: self.word_list.count(word) for word in self.word_list}
        max_value = max(occurrences.values())
        most_common = [key for key in occurrences if occurrences[key] == max_value]
        return (most_common, max_value)

    def unique_words(self):
        # find all the unique words
        unique_words = set(self.word_list)
        return list(unique_words)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            file_text = cls(file.read())
            return file_text


class TextModification(Text):
    STOP_WORDS = ["a", "an", "the", "in", "on", "is", "of", "and"]

    def __init__(self, text):
        super().__init__(text)
        self.text = self.text.lower()  # Convert to lowercase
        self.text = self.remove_punctuation()  # Remove punctuation
        self.text = self.remove_stop_words()  # Remove stop words
        self.word_list = self.text.split()

    def remove_punctuation(self):
        cleaned = self.text.translate(str.maketrans("", "", string.punctuation))
        return cleaned

    def remove_stop_words(self):
        words = self.text.split(" ")
        filtered_words = [word for word in words if word not in self.STOP_WORDS]
        new_text = ",".join(filtered_words)
        return new_text

    def remove_special_characters(self):
        pattern = re.compile(r"[^a-zA-Z0-9\s]")
        cleaned_text = pattern.sub("", self.text)
        return cleaned_text


# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP (Classes, Class Methods, Inheritance)
# Modules (File Handling, String Manipulation, Data Structures)
# Text Analysis Techniques


# Key Python Topics:

# OOP (Classes, Class Methods, Inheritance)
# File handling (open())
# String manipulation (split(), join(), translate(), regular expressions)
# Dictionaries
# Sets
# Lists
# string module
# re module (regular expressions)


# Instructions:

# Create a Text class to analyze text data, either from a string or a file. Then, create a
# TextModification class to perform text cleaning.


# Part I: Analyzing a Simple String

# Step 1: Create the Text Class

# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute
# (e.g., self.text).


# Step 2: Implement word_frequency Method

# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.


# Step 3: Implement most_common_word Method

# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.


# Step 4: Implement unique_words Method

# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.


# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method

# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.


# Bonus: Text Modification

# Step 6: Create the TextModification Class

# Create a class called TextModification that inherits from Text.


# Step 7: Implement remove_punctuation Method

# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.


# Step 8: Implement remove_stop_words Method

# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.


# Step 9: Implement remove_special_characters Method

# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.
