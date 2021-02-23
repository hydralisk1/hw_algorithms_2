def fibonacci(n):
    if type(n) is not int or n < 0:
        raise ValueError("The element has to be an integer number equal to or greater than 0")

    return n if 0 <= n <= 1 else fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))