"""
# open a file
f = open('a.txt', 'w')

# getting some infos
print('name = ', f.name)
print('it it closed? ', f.closed)
print('node = ', f.mode)
f.write('Python is my favorite language. ')
f.close()


# appending to a file
f = open('a.txt', 'a')
f.write('I also love Java')
f.close()


# r+ functionality
f = open('a.txt', 'r+')
info = f.read()
print(info)
f.close()
"""
# w+ mood --> remove previse text and add new test

f = open('a.txt', 'w+')
f.write('All is lost!!')
f.close()