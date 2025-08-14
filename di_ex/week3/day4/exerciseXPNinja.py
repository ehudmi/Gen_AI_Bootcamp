# What you will learn
# Dunder Methods
# Classes/Objects


# Exercise 1 : Temperature
# Instructions
# Write a base class called Temperature.
# Implement the following subclasses: Celsius, Kelvin, Fahrenheit.
# Each of the subclasses should have a method which can convert the temperature to another type.
# You must consider different designs and pick the best one according to the SOLID Principle.

from abc import ABC, abstractmethod


class Temperature(ABC):
    """Abstract class for temperature types"""

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def to_celsius(self):
        pass

    @abstractmethod
    def to_fahrenheit(self):
        pass

    @abstractmethod
    def to_kelvin(self):
        pass

    def __str__(self):
        return f"{self.value:.2f} degrees {self.__class__.__name__}"


class Celsius(Temperature):
    def to_celsius(self):
        return self.value

    def to_fahrenheit(self):
        return (self.value * 9 / 5) + 32

    def to_kelvin(self):
        return self.value + 273.15


class Fahrenheit(Temperature):
    def to_celsius(self):
        return (self.value - 32) * 5 / 9

    def to_fahrenheit(self):
        return self.value

    def to_kelvin(self):
        return (self.value - 32) * 5 / 9 + 273.15


class Kelvin(Temperature):
    def to_celsius(self):
        return self.value - 273.15

    def to_fahrenheit(self):
        return (self.value - 273.15) * 9 / 5 + 32

    def to_kelvin(self):
        return self.value


def convert_temperature(temp_type, temp_value):
    """Converts a temperature from a given type to others and prints the result."""

    temp_map = {1: Fahrenheit, 2: Celsius, 3: Kelvin}

    try:
        # Create an instance of the correct temperature class
        temp_object = temp_map[temp_type](temp_value)
    except KeyError:
        print("Invalid temperature scale selection.")
        return

    # Perform conversions and print results
    print(f"\nOriginal: {temp_object}")
    print(f"In Celsius: {temp_object.to_celsius():.2f} degrees Celsius")
    print(f"In Fahrenheit: {temp_object.to_fahrenheit():.2f} degrees Fahrenheit")
    print(f"In Kelvin: {temp_object.to_kelvin():.2f} degrees Kelvin")


# --- Main execution block ---
try:
    user_temp_str = input(
        "Please select temperature scale:\n1. Fahrenheit\n2. Celsius\n3. Kelvin\n"
    )
    user_temp = int(user_temp_str)

    temp_value_str = input("Please enter the value to convert\n")
    temp_value = float(temp_value_str)

    convert_temperature(user_temp, temp_value)

except ValueError:
    print("You did not input the right values.")

# Exercise 2: In the Quantum Realm
# Instructions
# Write a class called QuantumParticle and implement the following:
# The attributes - The particle has an initial position (x), momentum (y) and spin (p)

# The method position() - Position measurement: generate a random position (integer between 1 and
# 10,000)

# The method momentum() - Momentum measurement: generate a random momentum (float - a number between 0
# and 1)

# The method spin() - Spin measurement: can randomly be 1/2 or -1/2

# Create a method that implements a disturbance. A disturbance occurs each time a measurement is made
# (e.g. one of the measurements method is called). Disturbance changes the position and the momentum
# of the particle (randomly generated) and then prints ‘Quantum Interferences!!’

# Implement a meaningful representation of the particle (repr)

# Quantum Entanglement: two particle can be entangled, meaning that if I measure the spin of one of
# them the second one is automatically set to the opposite value. A quantum particle can only be
# entangled to another quantum particle (check that when you run the method !!)
# Modify as you see fit the attributes and methods of your class to fit the previous definition
# When two particles are entangled print: ‘Spooky Action at a Distance !!’
# >>>p1 = QuantumParticle(x=1,p=5.0)
# >>>p2 = QuantumParticle(x=2,p=5.0)
# >>>p1.entangle(p2)
# >>>'Particle p1 is now in quantum entanglement with Particle p2'
# >>>p1 = QuantumParticle()
# >>>p2 = QuantumParticle()
# >>>p1.entangle(p2)
# >>>'Spooky Action at a Distance'
