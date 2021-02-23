def remove_zeros(n):
    if type(n) is not int:
        raise ValueError("The element has to be an integer number")
    
    while n % 10 == 0 and n != 0:
        n //= 10

    return n

assert remove_zeros(1450) == 145
assert remove_zeros(96000) == 96
assert remove_zeros(1050) == 105
assert remove_zeros(-1050) == -105
assert remove_zeros(0) == 0