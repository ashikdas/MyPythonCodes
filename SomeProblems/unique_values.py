# A program to print the unique values in a dictionary
a = {1: 1, 2: 2, 3: 1, 4: 34, 5: 25, 6: 7}
b = {}
count = {}

for i in a.values():
    count.setdefault(i, 0)
    count[i] = count[i]+1

i = 0

for k, v in count.items():
    if v == 1:
        b.update({i: k})
        i = i+1

for i in b.values():
    print(i, end=" ")