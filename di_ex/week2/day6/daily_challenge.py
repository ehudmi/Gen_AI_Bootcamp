# Instructions: Old MacDonald’s Farm

# You are given example code and output. Your task is to create a Farm class that produces the
# same output.


# Step 1: Create the Farm Class

# Create a class called Farm.
# This class will represent a farm and its animals.


# Step 2: Implement the __init__ Method

# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes: name to store the farm’s name and animals to store the
# animals (initialize as an empty dictionary).

# Step 3: Implement the add_animal Method

# Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). Count is the
# quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

# Step 4: Implement the get_info Method

# Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and
# the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.


class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals.keys():
            self.animals[animal_type] += 1
        else:
            self.animals.update({animal_type: count})

    def get_info(self):
        farm_list = ""
        for k, v in self.animals.items():
            farm_list += f"{k} : {v}\n"
        info = f"{self.name}`s farm\n\n{farm_list}\nE-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animals_string = ""
        for index, item in enumerate(self.get_animal_types()):
            if index == len(self.get_animal_types()) - 1:
                if item == "sheep" or self.animals[item] == 1:
                    animals_string += f"and {item}"
                else:
                    animals_string += f"and {item}s"

            else:
                if self.animals[item] == 1 or item == "sheep":
                    animals_string += f"{item}, "
                else:
                    animals_string += f"{item}s, "
        return f"{self.name.capitalize()}`s farm has {animals_string}."


# Step 5: Test Your Code

# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.


# Example:

# class Farm:
#     def __init__(self, farm_name):
#         # ... code to initialize name and animals attributes ...

#     def add_animal(self, animal_type, count):
#         # ... code to add or update animal count in animals dictionary ...

#     def get_info(self):
#         # ... code to format animal info from animals dictionary ...


# # Test the code
macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
# #output:
# # McDonald's farm

# # cow : 5
# # sheep : 2
# # goat : 12

# #     E-I-E-I-0!


# Bonus: Expand The Farm


# Step 6: Implement the get_animal_types Method

# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
# Use the sorted() function to sort the list.


# Step 7: Implement the get_short_info Method

# Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name if its count is greater than 1.
# Use string formatting to create the output.
