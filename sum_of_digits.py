def sum_of_digits(n):
    if type(n) is not int or n <= 0:
        raise ValueError("The element has to be one of the natural numbers")

    result = 0

    while n > 0:
        result += n % 10
        n //= 10
    
    return result if result < 10 else sum_of_digits(result)

# Get the result using convert the element of this function from int to str
def sum_of_digits_str(n):
    if type(n) is not int or n <= 0:
        raise ValueError("The element has to be one of the natural numbers")
    
    result = sum([int(c) for c in str(n)])
    
    return result if result < 10 else sum_of_digits_str(result)

assert sum_of_digits(16) == 7
assert sum_of_digits(942) == 6
assert sum_of_digits(132189) == 6
assert sum_of_digits(493193) == 2

assert sum_of_digits_str(16) == 7
assert sum_of_digits_str(942) == 6
assert sum_of_digits_str(132189) == 6
assert sum_of_digits_str(493193) == 2