# symmetric triangle
'''
   *
  ***
 *****
*******
'''

'''
row = int(input())

count = 0
for i in range(0, row):
    for j in range(0, row-i-1):
        print(end=" ")

    count = count+1
    for k in range(0, i+count):
        print("*", end= "")
    print(" ")
'''



'''
   *
  **
 ***
****
'''

row = int(input())
for i in range(0, row):
    for j in range(0, row-1-i):
        print(end=" ")
    for k in range(0, i+1):
        print("*", end="")

    print(" ")



