# fibonacci sequence:
# 0 1 1 2 3 5 8 13 ......

n = int(input('Enter the number of sequence: '))
def fibonacci(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        print(x)
        print(y)
        for i in range(1,n):
            z = x+y
            x = y
            y = z
            print(z)

fibonacci(n)
