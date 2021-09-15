# This program simulates a phone-book
contact_no = {'Sam': 000, 'Smith': 1111, 'Ron': 2222}
x = 0

while x < 5:
    print('Enter your Name(press ENTER to exit): ')
    name = input()

    if name == '':
        break

    if name in contact_no:
        print('The contact number of '+name+' is '+str(contact_no[name]))
    else:
        print('There is no such name in the phone book. Do you want to add it?')
        desc = input()

        if desc == 'yes':
            print('Enter the Number: ')
            number = input()
            contact_no[name] = number
            print('Phone Book Updated.')
        elif desc == 'no':
            print('Do you want to quit?')
            desc == input()
            if desc == 'yes':
                break
            else:
                print('Keep Searching.')
    x = x+1