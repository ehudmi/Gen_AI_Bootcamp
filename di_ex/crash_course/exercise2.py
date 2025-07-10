human_years = int(input("How many years ago did you get the puppy and the kitten?\n"))
if human_years == 1:
    dog_years = 15
    cat_years = 15
elif human_years == 2:
    dog_years = 15 + 9
    cat_years = 15 + 9
else:
    dog_years = 15 + 9 + 5 * (human_years - 2)
    cat_years = 15 + 9 + 4 * (human_years - 2)

print([human_years, cat_years, dog_years])
