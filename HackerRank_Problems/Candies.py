def candies(n, arr):
    candies_count = [1] * n
    for i in range(n - 1):
        if arr[i + 1] > arr[i]:
            candies_count[i + 1] = candies_count[i] + 1
    for i in range(n - 1, 0, -1):
        if arr[i - 1] > arr[i] and candies_count[i - 1] <= candies_count[i]:
            candies_count[i - 1] = candies_count[i] + 1
    return sum(candies_count)


result = candies(8, [2, 4, 3, 5, 2, 6, 4, 5])
print(result)
