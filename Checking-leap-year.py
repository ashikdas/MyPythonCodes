# leap year check

year = int(input('Enter the year to check: '))
if year % 400 ==0:
    print('It is a leap year.')
elif year % 100 ==0:
    print('It is not a leap year.')
elif year % 4 ==0:
    print('It is a leap year.')
else:
    print('It is not a leap year.')