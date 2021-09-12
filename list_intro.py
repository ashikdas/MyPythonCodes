'''
# making a list
a = [1, 2, 3]
b = ['a', 'b', 'c']
z = [3.1416, 'pi', 23]

print(z)
print(a[2])

# Nested Lists
x = [[1, 2, 3], [4, 5, 6]]

print(x[1][1])

# Negative indexes
p = [1, 2, 3, 4]
print(p[-1])
print(p[-2])


# sub lists and slicing
q = [1, 2, 3, 4, 5, 6]
print(q[0:5])
# q[starting_index : end_index+1]
# q[0:4+1]
print(q[0:-2])
print(q[1:-1]) # will print 1 to before -1
print(q[:4]) # will print 0 to 3
print(q[1:]) # will print 1 to end
print(q[:]) # will print all values

# adding 2 list
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
ab = a+b
print(ab)

# making double of list element
x = ['p', 'q', 'r']
new_x = x*2
print(new_x)

# deleting list element
p = ['a', 'b', 'c']
del p[0]
print(p)
'''
