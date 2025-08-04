def fib(number):
    """Returns fibonacci numbers until the number"""
    fib_list = [0, 1]
    for i in range(2, number + 1):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    return fib_list


print(fib(20))
