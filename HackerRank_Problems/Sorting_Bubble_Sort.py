def countSwaps(a):
    count = 0
    for i in range(0, len(a)):
        for j in range(0, len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


countSwaps([3, 2, 1])
