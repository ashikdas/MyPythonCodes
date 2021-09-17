# Digit counting

def digit_counting(n):
    if n == 0:
        return 0
    return 1 + digit_counting(n // 10)


print(digit_counting(1234))
