name = input("What is your name?\n")
password = input("Select a password\n")
print(
    f"Hi {name}, Your password {'*'*len(password)} is {len(password)} characters long"
)
