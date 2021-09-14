# printing the odds:

def print_odd(some_list):
    new_list = []

    for i in range(len(some_list)):
        if some_list[i] % 2 != 0:
            new_list.append(some_list[i])

    return new_list


a = [1, 2, 5, 9, 10, 16, 19, 21, 32]
print(print_odd(a))