# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = 0
# for i in my_list:
#     a = a + i
# print(a)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i, char)
