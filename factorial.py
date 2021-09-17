# Simple recursion example using factorial calculation

def factorial(n):
    temp = 1
    for i in range(2, n + 1):
        temp = temp * i

    return temp


# Recursion
def factorial_rec(n):
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)


num = input()
print(factorial(int(num)))

print(factorial_rec(int(num)))
