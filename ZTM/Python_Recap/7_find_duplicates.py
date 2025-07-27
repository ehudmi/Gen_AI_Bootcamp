# some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
# dup_list = []
# for char in some_list:
#     if some_list.count(char) > 1 and dup_list.count(char) < 1:
#         dup_list.append(char)
#     else:
#         continue
# print(dup_list)

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)

duplicates = list(set([item for item in some_list if some_list.count(item) > 1]))
print(duplicates)
