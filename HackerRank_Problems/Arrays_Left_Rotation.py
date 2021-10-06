def rotLeft(a, d):
    rotated_arr = []
    for i in range(d, len(a)):
        rotated_arr.append(a[i])
    for i in range(0, d):
        rotated_arr.append(a[i])

    return rotated_arr


result = rotLeft([1, 2, 3, 4, 5], 4)
print(result)
