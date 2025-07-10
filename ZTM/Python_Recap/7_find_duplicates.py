some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
dup_list = []
for char in some_list:
    if some_list.count(char) > 1 and dup_list.count(char) < 1:
        dup_list.append(char)
    else:
        continue
print(dup_list)
