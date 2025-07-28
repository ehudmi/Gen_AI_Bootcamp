# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You

input_str = "You have entered a wrong domain"
string_list = input_str.split(" ")
output_str = " ".join(string_list[::-1])
print(output_str)
