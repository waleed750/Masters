# Exercise (2) :-

import math


def ex_1():
    a = float(input('Enter the Value of (A): '))
    b = float(input('Enter the Value of (B): '))
    c = float(input('Enter the Value of (C): '))
    d = math.pow(b, 2) - (4 * a * c)
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    if d > 0:
        print('The Equation has Two Real Roots, And The Discriminant Value is:', d)
        print('The First Real Root is:', r1)
        print('The Second Real Root is:', r2)
    elif d == 0:
        print('The Equation has One Real Root, And The Discriminant Value is:', d)
        print('The First & Second Real Roots are Equal: ', 'r1 = ', r1, ', r2 = ', r2)
    elif d < 0:
        print('The Equation has No Real Roots, And The Discriminant Value is:', d)


def ex_2():
    x = int(input('Enter an Integer Value of (X): '))
    y = int(input('Enter an Integer Value of (Y): '))
    z = int(input('Enter an Integer Value of (Z): '))
    if (x + y) > z and (y + z) > x and (x + z) > y:
        if x == y or y == z or x == z:
            print('The Triangle with Sides (', x, y, z, ') is {Isosceles}')
        elif x == y and y == z and x == z:  # x == y == z
            print('The Triangle with Sides (', x, y, z, ') is {Equilateral}')
        elif x != y and y != z and x != z:
            print('The Triangle with Sides (', x, y, z, ') is {Scalene}')
    else:
        print('The Triangle with Sides (', x, y, z, ') is {Not a Triangle}')


def ex_3():
    m = int(input('Enter the Month: '))
    y = int(input('Enter the Year: '))
    if m == 1:
        print('January ' + str(y) + ' has 31 Days.')
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            print('February ' + str(y) + ' (Leap Year) has 29 Days.')
        else:
            print('February ' + str(y) + ' (Not Leap Year) has 28 Days.')
    elif m == 3:
        print('March ' + str(y) + ' has 31 Days.')
    elif m == 4:
        print('April ' + str(y) + ' has 30 Days.')
    elif m == 5:
        print('May ' + str(y) + ' has 31 Days.')
    elif m == 6:
        print('June ' + str(y) + ' has 30 Days.')
    elif m == 7:
        print('July ' + str(y) + ' has 31 Days.')
    elif m == 8:
        print('August ' + str(y) + ' has 31 Days.')
    elif m == 9:
        print('September ' + str(y) + ' has 30 Days.')
    elif m == 10:
        print('October ' + str(y) + ' has 31 Days.')
    elif m == 11:
        print('November ' + str(y) + ' has 30 Days.')
    elif m == 12:
        print('December ' + str(y) + ' has 31 Days.')
    else:
        return 'Error, Not-Month'


def ex_4():
    n = int(input('Enter an Integer Number between (0 - 1000): '))
    s = 0
    if 0 <= n <= 1000:  # n >= 0 and n <= 1000
        for i in str(n):
            s += int(i)
        print('The Sum of All Digits you Entered is: ', s)
    else:
        print('Not-Found, Please, Enter an Integer Number between (0 and 1000).')


def main():
    # print(math.e)
    ex_1()
    # ex_2()
    # ex_3()
    # ex_4()


main()
