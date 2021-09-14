f = open('NUMBERS', 'w+')
f.write('123321')
f.close()

f = open('NUMBERS', 'r+')
some_list = list(f.read())
f.close()

is_palindromic = True

for i in range(int(len(some_list)/2)):
    if some_list[i] != some_list[len(some_list)-i-1]:
        is_palindromic = False


if is_palindromic:
    f =open('NUMBERS','a')
    f.write('YES')
    f.close()
else:
    f = open('NUMBERS', 'w')
    for i in range(len(some_list)):
        f.write('0')