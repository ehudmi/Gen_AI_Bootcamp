# Exercise 1
# Given the list:

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# 1. Print the first element from the list.

print(fruits[0])

# 2. Print the third element from the list.

print(fruits[2])

# 3. Try accessing an element at an index that doesn't exist (e.g., the 6th element) and note what happens.

# print(fruits[6])

# 4. Change the second fruit ("banana") to "blueberry".

# fruits[1] = "blueberry"
# print(fruits[1])

# Exercise 2
# Using the same list from the previous exercise:

# 1. Add "fig" to the end of the fruits

# fruits.append("fig")
# print(fruits)

# 2. Insert "grape" at the beginning of the list

# fruits.insert(0, "grape")
# print(fruits)

# 3. Remove "cherry" from the list using using the specific method for it

# fruits.remove("cherry")
# print(fruits)

# 4. Remove the last element from the list using the specific method for it

# fruits.pop()
# print(fruits)

# 5. Create another list of berries and combine it with the fruits list into a list called "combined_list"

fruits_1 = ["oranges", "strawberry", "clementine"]
combined_list = fruits.copy()
combined_list.extend(fruits_1)
print(combined_list)

# 6. Sort the combined_list

combined_list.sort()

# 7. Slice the last three elements of the combined list

print(combined_list[-3:])
