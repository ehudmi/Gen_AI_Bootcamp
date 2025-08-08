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
import turtle as t


class Circle:
    def __init__(self, **kwargs):
        if "radius" in kwargs.keys():
            self.radius = kwargs["radius"]
        if "diameter" in kwargs.keys():
            self.radius = kwargs["diameter"] / 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"I am a circle and my radius is {self.radius} and my diameter is {self.diameter} and my area is {self.area:.2f}"

    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("You are not adding a circle object")
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)

    def __gt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("You are not comparing to a circle object")
        return self.radius > other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("You are not comparing to a circle object")
        return self.radius < other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("You are not comparing to a circle object")
        return self.radius == other.radius

    @classmethod
    def sort_circles(cls, circle_list):
        """class method for sorting circles"""
        if not isinstance(circle_list, list):
            raise TypeError("You did not provide a list")
        for circle in circle_list:
            if not isinstance(circle, cls):
                raise TypeError("One of the items is not a Circle")
        return sorted(circle_list)

    @classmethod
    def draw_circle(cls, circle_list):
        if not isinstance(circle_list, list):
            raise TypeError("You did not provide a list")
        for circle in circle_list:
            if not isinstance(circle, cls):
                raise TypeError("One of the items is not a Circle")
            t.penup()
            t.goto(0, -circle.radius)  # Center the circle on the screen
            t.pendown()
            t.circle(circle.radius)


circle1 = Circle(radius=5)
circle2 = Circle(diameter=12)
circle3 = Circle(radius=8)
circle4 = Circle(radius=2)
print(circle1)
print(circle2)
print(circle1 + circle2)
print(circle1 > circle2)
print(circle2 > circle1)
# print(circle1 + 5)
sorted_list = Circle.sort_circles([circle1, circle2, circle3, circle4])
Circle.draw_circle(sorted_list)
