# What You will learn :
# OOP dunder methods


# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder
# method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

import math


class Circle:
    def __init__(self, **kwargs):
        if "radius" in kwargs.keys():
            self.radius = kwargs["radius"]
        if "diameter" in kwargs.keys():
            self.radius = kwargs["diameter"] / 2
        self.area = math.pi * self.radius**2

    def __str__(self):
        return f"I am a circle and my radius is {self.radius} and my diameter is {self.radius*2} and my area is {self.area:.2f}"

    def __add__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            new_circle = Circle(radius=new_radius)
            return new_circle
        else:
            raise TypeError("You are not adding a circle object")

    def __gt__(self, other):
        if isinstance(other, Circle):
            if self.radius > other.radius:
                return True
            else:
                return False
        else:
            raise TypeError("You are not adding a circle object")

    def __eq__(self, other):
        if isinstance(other, Circle):
            if self.radius == other.radius:
                return True
            else:
                return False
        else:
            raise TypeError("You are not adding a circle object")

    @classmethod
    def sort_circles(cls, circle_list):
        """class method for sorting circles"""
        if not isinstance(circle_list, list):
            raise TypeError("You did not provide a list")
        n = len(circle_list)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if not isinstance(circle_list[j], cls):
                    raise TypeError("One of the items is not a Circle")
                if circle_list[j] > circle_list[j + 1]:
                    circle_list[j], circle_list[j + 1] = (
                        circle_list[j + 1],
                        circle_list[j],
                    )
                    swapped = True
                if not swapped:
                    break
        return circle_list


circle1 = Circle(radius=5)
circle2 = Circle(diameter=12)
print(circle1)
print(circle2)
print(circle1 + circle2)
print(circle1 > circle2)
print(circle2 > circle1)
# print(circle1 + 5)
print(Circle.sort_circles([circle2, circle1]))
