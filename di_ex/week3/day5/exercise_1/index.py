# Retrieve the data into the python file, inside a variable called family
# Print nicely the details about Jane's children
# Inside the family variable, add to each children, a key favorite_color with a value
# Then, save back all the new data into the json file
# Use the indent argument inside the dump function. Check out the documentation and the video in
# the Useful Resources

from pathlib import Path
import json

path_location = Path(__file__).parent / "file.json"
with open(path_location, "r") as file_obj:
    family = json.load(file_obj)
    for child in family["children"]:
        print(f"{child['firstName']} is {child['age']} years old")
        child["favorite_color"] = "red"
        print(child)
    with open(path_location, "w") as file_obj:
        json.dump(family, file_obj, indent=2)
