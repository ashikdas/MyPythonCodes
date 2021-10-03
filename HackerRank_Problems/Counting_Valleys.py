def countingValleys(steps, path):
    current_level = 0
    count = 0
    for i in range(steps):
        if path[i] == 'U':
            current_level += 1
        elif path[i] == 'D':
            current_level -= 1
            if current_level == -1:
                count += 1
    return count


result = countingValleys(8, 'DUUDDUDD')
print(result)
