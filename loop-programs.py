# use of infinite loop
"""
while True:
    print('Enter your Name: ')
    name = input()
    if name == 'Ashik':
        break
print('Thank You')
"""

# Use of Continue Statement:
"""
while True:
    print('What is your Name? ')
    name = input()
    if name != 'Ashik':
        continue
    print('Hello There'+name+'. What is the passcode?')
    passcode=input()
    if passcode == 'icecream':
        break
print('Thank You!')
"""

# series: 1+2+3+4
"""
sum = 0
for i in range(1,5):
    sum = sum+i

print(sum)
"""

# series: 1^2+2^2+3^2+4^2
"""
sum = 0
for i in range(1,5):
    sum = sum+i*i

print('Sum: '+str(sum))
"""

# Series: 1+3+5+7+9
"""
odd_sum = 0
for i in range(1,10,2):
    odd_sum=odd_sum+i

print(odd_sum)
"""

# Even_Series: 2+4+6+8
"""
Even_sum = 0
for i in range(2,10,2):
    Even_sum=Even_sum+i

print(Even_sum)
"""

# Complex series = 1+(1+2)+(1+2+3)+(1+2+3+4)

sum = 0
for i in range(1,5):
    for j in range(1,i+1):
        sum = sum+j

print(sum)




