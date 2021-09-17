# Reverse a list

def reverse_list(a):
    new_list = []

    # for i in range(0, len(a)):
    #  new_list.append(0)

    for i in range(len(a) - 1, -1, -1):
        # new_list[len(a) - 1 - i] = a[i]
        new_list.append(a[i])

    return new_list


# In Recursive way
def reverse_list_recursive(some_list):
    if len(some_list) == 0:
        return []
    return [some_list[-1]] + reverse_list_recursive(some_list[:-1])


lists = [1, 2, 3, 4, 5]

print(reverse_list_recursive(lists))
