# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****

# for i in range(1, 6, 2):
#     print(f"{' '*int(3-i/2)}{'*'*i}{' '*int(3-i/2)}")

# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****

# for i in range(1, 6):
#     print(f"{' '*int(5-i)}{'*'*i}")

# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *
# for i in range(1, 6):
#     print(f"{'*'*i}{' '*int(5-i)}")
# for i in range(5, 0, -1):
#     print(f"{' '*int(5-i)}{'*'*i}")

# Exercise 2
# Instructions
# Analyse this code before executing it. Write some comments next to each line. Write the value of each
# variable and their changes, and add the final output. Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):  # checking for every index in the list
    minimum = i
    for j in range(i + 1, len(my_list)):  # checking for the next item in the list
        if (
            my_list[j] < my_list[minimum]
        ):  # if the next item is smaller than the one before
            minimum = j  # the index of the smaller item is the new minimum
            if minimum != i:
                my_list[i], my_list[minimum] = (
                    my_list[minimum],
                    my_list[i],
                )  # sorts the list in place
print(my_list)
