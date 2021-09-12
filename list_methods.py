places_visited = ['India', 'Nepal', 'Malaysia', 'Bhutan', 'USA', 'maldip', 'europ']

"""
# the list methods:
# index() method --> Return index number
print(places_visited.index('Bhutan'))

# append() --> add new element in the list

places_visited.append('Africa')
print(places_visited)

# insert () --> insert new value in specific index
places_visited.insert(2, 'UK')
print(places_visited)

# remove () --> remove element
places_visited.remove('Nepal')
print(places_visited)

# sort () --> to sort element according ASC/DSC

places_visited.sort()
print(places_visited)

# to sort alphabetically:
places_visited.sort(key=str.lower)
print(places_visited)
"""
# short in reverse way
places_visited.sort(key=str.lower, reverse=True)
print(places_visited)
