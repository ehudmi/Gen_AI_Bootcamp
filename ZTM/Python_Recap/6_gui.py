picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for list_item in picture:
    index = 0
    while index < len(list_item):
        if list_item[index] == 0:
            list_item[index] = " "
            index += 1
        else:
            list_item[index] = "*"
            index += 1
    print("".join(list_item))
