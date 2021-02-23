def remove_zeros(n):
    if type(n) is not int:
        raise ValueError("The element has to be an integer number")

    return n if n == 0 or n % 10 != 0 else remove_zeros(n // 10)

# Get the result using convert the element from int to str
def remove_zeros_str(n):
    if type(n) is not int:
        raise ValueError("The element has to be an integer number")
    
    if n == 0:
        return n

    n = str(n)
    for c in n[::-1]:
        if c == "0":
            n = n[:-1]
        else:
            return int(n)

assert remove_zeros(1450) == 145
assert remove_zeros(96000) == 96
assert remove_zeros(1050) == 105
assert remove_zeros(-1050) == -105
assert remove_zeros(0) == 0

assert remove_zeros_str(1450) == 145
assert remove_zeros_str(96000) == 96
assert remove_zeros_str(1050) == 105
assert remove_zeros_str(-1050) == -105
assert remove_zeros_str(0) == 0