print('Enter your Number: ', end="")
digit = int(input())
temp = digit
sum = 0


while digit !=0:
    digit_mod = digit % 10
    digit = digit//10
    sum = sum + digit_mod**3

if sum == temp:
    print('The Number is Armstrong.')
else:
    print('The Naumber is not Armstrong.')