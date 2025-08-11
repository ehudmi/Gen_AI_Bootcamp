from random import randint as rand
from sys import argv as argv


def guess_random(range_start=int(argv[1]), range_end=int(argv[2])):

    if int(argv[1]) and int(argv[2]):
        comp_number = rand(int(argv[1]), int(argv[2]))
    else:
        comp_number = rand(1, 10)
    while True:
        try:
            user_number = int(
                input(
                    f"please guess a number in the range {range_start} - {range_end}\n"
                )
            )
            if user_number >= range_start and user_number <= range_end:
                break
            else:
                print(
                    f"The number you chose is not in the range {range_start} - {range_end}"
                )
                continue
        except:
            print("The value you input is not a number")
            continue

    if user_number == comp_number:
        return print("You are a genius")
    else:
        return print("Better luck next time")


guess_random()
