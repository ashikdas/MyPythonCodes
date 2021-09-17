# Calculating sum of a series

def sum_f(n):
    sum = 0

    for i in range(1, n+1):
        sum = sum + i

    return sum


print(sum_f(6))


# Using recursion:

def sum_rec(n):
    if n == 0:
        return 0

    return n+sum_rec(n-1)


print(sum_rec(10))