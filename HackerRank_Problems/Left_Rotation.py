def rotateLeft(d, arr):
    rotated_arr = []
    for i in range(d, len(arr)):
        rotated_arr.append(arr[i])
    for i in range(0, d):
        rotated_arr.append(arr[i])

    return rotated_arr


result = rotateLeft(4, [1, 2, 3, 4, 5])
print(result)
