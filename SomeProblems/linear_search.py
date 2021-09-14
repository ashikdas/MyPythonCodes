# linear search

def linear_search(some_list, value):
    for i in range(len(some_list)):
        if some_list[i] == value:
            return "FOUND"

    if i == len(some_list)-1:
        return "NOT FOUND"


a = [1, 2, 3, 4, 5, 6]
print(linear_search(a, 3))
print(linear_search(a, 7))
