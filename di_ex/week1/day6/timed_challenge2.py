# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print
# True else False.
# Hint: Google perfect numbers
# Example

aliquot_sum = 0
user_input = int(input("Give me a number\n"))
for i in range(1, user_input):
    if user_input % i == 0:
        aliquot_sum += i
    else:
        continue
print(True if aliquot_sum == user_input else False)

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False
