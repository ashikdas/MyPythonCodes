# printing fibonacci series using recur

def recursive_fibonacci(n):
    if n <= 1:
        return n

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


print(recursive_fibonacci(5))
