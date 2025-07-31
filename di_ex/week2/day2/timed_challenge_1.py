def find_char(char, string):
    count_char = 0
    for i in string:
        if i == char:
            count_char += 1
    return count_char


print(find_char("o", "Programming is cool!"))
