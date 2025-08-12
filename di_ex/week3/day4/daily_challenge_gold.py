# What You will learn :
# OOP


# Instruction: Information from the user
# Harder Daily Challenge
# Notice : solve this exercise using a lambda function.

# Ask a user for the following inputs 5 times:
# Name (string)
# Age (int)
# Score (int)
# Build a list of tuples using these inputs, each tuple should contain a name, age and score.
# Sort the list by the following priority Name > Age > Score.
# If the following tuples are given as input to the script:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'),
# ('Tom', '19', '80')]
# Note : The lambda function will not print but sort


def collect_info():
    counter = 5
    info_list = []
    while counter >= 1:
        user_input = input("Please enter Name, Age and Score separated by comma\n")

        info = user_input.split(",")
        if not info[0].isalpha():
            raise TypeError("The name you provided is not a string")
        else:
            try:
                info[1] = int(info[1])
                info[2] = int(info[2])
            except ValueError:
                print("the age or score provided are not numbers")
            new_tuple = tuple(i for i in info)
            info_list.append(new_tuple)
            counter -= 1
    sorted_info = sorted(info_list, key=lambda tup: (tup[0], tup[1], tup[2]))
    return print(sorted_info)


collect_info()
