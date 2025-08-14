# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# A class is a blueprint for creating objects with predefined attributes and methods

# What is an instance?
# An instance is an object based on the blueprint of the class

# What is encapsulation?
# encapsulation is the creation of objects that can handle both attributes and methods to manage
# data

# What is abstraction?
# abstraction is using an attribute or method without being exposed to the way they were
# implemented

# What is inheritance?
# inheritance is when the object created on the basis of a class receives attributes and
# methods from the parent class or when a class inherits from a parent class

# What is multiple inheritance?
# multi-inheritance is when an object inherits from more than one class - either directly or
# indirectly if the classes he is inheriting from are also based on other classes and inheriting
# from them

# What is polymorphism?
# polymorphism is when a method can behave differently when called by different object classes
# even if the classes share the same method name

# What is method resolution order or MRO?
# MRO is the way python handles multi-inheritance and the way it decides who takes precedence in
# determining whose inheritance the object will receive


# Part 2: Create a deck of cards class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:
from random import shuffle, randint


class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []
        for i in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for j in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                card = Card(i, j)
                self.cards.append(card)

    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)
        else:
            raise Exception("The deck does not contain 52 cards")

    def deal(self):
        index = randint(0, len(self.cards) - 1)
        print(
            f"The card you were dealt is {self.cards[index].suit} - {self.cards[index].value}"
        )
        self.cards.remove(self.cards[index])
        print(len(self.cards))


# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value
# (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then
# rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt,
# it should be removed from the deck.

my_deck = Deck()
my_deck.deal()

# my_card = Card("Hearts", "2")
# print(my_card.suit)
