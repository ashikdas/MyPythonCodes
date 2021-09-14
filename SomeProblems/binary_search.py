# binary search

def binary_search(some_list, value):

    if value > some_list[-1]:
        return "NOT FOUND"

    first = 0
    last = len(some_list)-1

    while first <= last:
        mid = (first+last)//2

        if some_list[mid] == value:
            return "FOUND"
        elif some_list[mid] < value:
            first = mid+1
        elif some_list[mid] > value:
            last = mid-1

    if first > last:
        return "NOT FOUND"


a = [1, 2, 5, 9, 10, 16, 19, 21, 32]
print(binary_search(a, 16))
print(binary_search(a, 31))
