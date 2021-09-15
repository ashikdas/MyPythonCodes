# Banking System:
bank_users = {'Alice': 1200, 'Samee': 2596, 'Robert': 2770}

print('Welcome To the Banking System.')
while True:
    print('What do you like to do?')
    print('  '+'1. VIEW BALANCE')
    print('  '+'2. VIEW ALL BANK INFO')
    print('  '+'3. UPDATE BALANCE')
    print('  '+'4. EXIT')

    desc = input()
    if desc == '1':
        print('Enter your Name, Please: ')
        name = input()
        if name in bank_users.keys():
            print('Hello '+name+' your account balance is '+str(bank_users[name]))
        else:
            print('The use can not be found. Would you like to add the user to the banking system?')
            desc = input()
            if desc == 'yes':
                k = input('Enter your Name: ')
                v = int(input('Enter your balance: '))
                bank_users.update({k : v})
            else:
                print('Would you like to exit?')
                desc = input()
                if desc == 'yes':
                    break

    elif desc == '2':
        for k, v in bank_users.items():
            print('USERNAME: '+str(k)+' BANK BALANCE: '+str(v))

    elif desc == '3':
        print('Enter your Name, Please: ')
        name = input()
        if name in bank_users.keys():
            print('Do you want to add or subtract from your savings?')
            desc = input()
            if desc == 'add':
                temp_balance = bank_users[name]
                extra = input('Enter the amount you want to add: ')
                bank_users[name] = temp_balance + int(extra)
                print('Balance updated. New Balance is: '+str(bank_users[name]))
            elif desc == 'subtract':
                temp_balance = bank_users[name]
                extra = input('Enter the amount you want to add: ')
                bank_users[name] = temp_balance - int(extra)
                print('Balance updated. New Balance is: ' + str(bank_users[name]))

        else:
            print('There is no such account in the bank database.')

    elif desc == '4':
        break
