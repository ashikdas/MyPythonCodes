# this program simulates a password protected app access

password_bank = {'Sam': 1234, 'Smith': 909090, 'Ruth': 12345}
matched = False
x = 0

print("Enter Your Name: ")

while x < 5:
    name = input()
    if name in password_bank:
        for i in range(0, 3):
            print("Enter Your Password: ")
            password = input()
            if int(password) in password_bank.values():
                matched = True
                print("Access Granted!")
                break
            else:
                print('Wrong Password. Enter Again: '+' You have '+str(2-i)+' tries left')
    else:
        print('There is no such name in the password_bank. Try Again')
    x = x+1

    if matched:
        break