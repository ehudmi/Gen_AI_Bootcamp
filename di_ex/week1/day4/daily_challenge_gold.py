# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then
# add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !

# birthdate = input("Please enter your birthdate in the format DD/MM/YYYY\n")
# year = int(birthdate[-4:])
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print(
#         2
#         * f"""
#        {'_'*int((12-((2025-year)%10))/2)}{'i'*((2025-year)%10)}{'_'*int((12-((2025-year)%10))/2)}
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~
# """
#     )
# else:
#     print(
#         f"""
#        {'_'*int((12-((2025-year)%10))/2)}{'i'*((2025-year)%10)}{'_'*int((12-((2025-year)%10))/2)}
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~
# """
#     )
