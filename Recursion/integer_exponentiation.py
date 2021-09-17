# Calculating integer exponentiation: 2^3 = 8

def exponent(x, y):
    if y == 0:
        return 1
    else:
        return x * exponent(x, y - 1)


# print(exponent(2, 3))

def exponent2(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return exponent(x, y//2) * exponent(x, y//2)
    else:
        return x*exponent(x, y//2)*exponent(x, y//2)


print(exponent2(2,8))
