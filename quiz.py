
'''
y = 10
a = 20
b = 51

if a > 19:
    if b < 0:
        if y == 10:
            y = y + 111
    elif a > 5:
        y = y + 41
    else:
        y = y + 30
else:
    y = y + 22

print(y)
'''

'''
num = 0

for i in range(5):
    for j in range(0, -100, -1):
        num += 1

print(num)
'''
'''
x= 0
while (x < 100):
    x+=2
if x % 33 == 0:
    print(‘This is an awkward loop!’)
    '''
for i in range(1001, 2001, 202):
     for j in range(-15, -150, -2):
     for k in range(1, 10):
      print(i,j,k, end=’,’)