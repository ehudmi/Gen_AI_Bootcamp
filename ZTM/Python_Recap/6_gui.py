picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for i in range(len(picture)):
    for index, item in enumerate(picture[i]):
        if item == 0:
            picture[i][index] = " "
        else:
            picture[i][index] = "*"
    print("".join(picture[i]))
