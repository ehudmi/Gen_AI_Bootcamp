def highest_even(li=[]):
    max_val = 0
    for i in li:
        if i > max_val and i % 2 == 0:
            max_val = i
    return max_val


print(highest_even([10, 2, 3, 30, 4, 8, 11, 28]))
