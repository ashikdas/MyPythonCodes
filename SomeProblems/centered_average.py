# centered-average:

def centered_average(some_list):
    sum = 0
    count = 0
    temp_list = some_list.sort()
    for i in range(1, len(some_list)-1):
        sum = sum+some_list[i]
        print(some_list[i])
        count = count+1

    return sum/count


a = [21, 2, 5, 9, 10, 16, 19, 1, 32]
print(centered_average(a))