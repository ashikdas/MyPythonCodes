def area_func():
    print('Enter the shape to find the area(press Enter to exit): ')
    shape = input()

    if shape == 'CIRCLE':
        print('Please Enter the radious: ')
        r = float(input())
        area = 3.1416*r*r
        print('The area is: ', area)
    elif shape == 'TRIANGLE':
        print('Please Enter the base: ')
        base = float(input())
        height = float(input('Please Enter the height: '))
        area = 0.5*base*height
        print('The area is: ', area)
    elif shape == 'RECTANGLE':
        print('Please Enter the lenght: ')
        length = float(input())
        breadth = float(input('Please Enter the height: '))
        area = length * breadth
        print('The area is: ', area)

    elif shape == 'SQUARE':
        print('Please Enter the length: ')
        length = float(input())
        area = length**2
        print('The area is: ', area)
    elif shape == 'TRAPEZIUM':
        side1 = float(input('Please Enter the side 1: '))
        side2 = float(input('Please Enter the side 2: '))
        height = float(input('Please Enter the height: '))
        area = 0.5*(side1+side2)*height
        print('The area is: ', area)


area_func()