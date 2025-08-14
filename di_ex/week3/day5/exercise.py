# Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following
# steps


# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file
# Read all the file and return it as a list of strings. Then split each word into letters
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"
from pathlib import Path

path_location = Path(__file__).parent / "nameslist.txt"
# with open(path_location, "r") as file:
#     for line in file:
#         file.readline()
#     print("read all lines")

# with open(path_location, "r") as file:
#     line = file.readline(5)
#     print(f"fifth line is {line}")

# with open(path_location, "r") as file:
#     string = file.read(5)
#     print(f"first five chars are {string}")
# with open(path_location, "r") as file:
#     string_list = file.read().split()
#     counter = 0
#     for _ in string_list:
#         if _ == "Darth":
#             counter += 1
#     print(f"there are {len(string_list)} words in the file")
#     print(f"there are {counter} appearances of 'Darth' in the file")

# with open(path_location, "a") as file:
#     file.write("Ehud")

# Read all lines from the file
with open(path_location, "r") as file:
    lines = file.readlines()

# Make the changes in a new list
new_lines = []
for line in lines:
    if line.strip() == "Luke":
        new_lines.append("Luke Skywalker\n")
    else:
        new_lines.append(line)

# Write the new content back to the file, overwriting the old content
with open(path_location, "w") as file:
    file.writelines(new_lines)

print("File updated successfully.")
