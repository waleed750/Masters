# Exercise (7) :-

import fractions


def ex_1():
    with open('numbers.txt', 'w') as f:
        for i in range(1, 101):
            f.write(str(i) + '\n')


def sumFile(fileName):  # ex_2()
    s = 0
    with open(fileName, 'r') as f:
        for i in f:
            print(int(i.strip()), end=' ')
            s += int(i)
        print('\nThe Sum of All Integers Are:', s)


def ex_3():
    num1 = int(input('Enter the Numerator1: '))
    den1 = int(input('Enter the Denominator1: '))
    f1 = fractions.Fraction(num1, den1)
    num2 = int(input('Enter the Numerator2: '))
    den2 = int(input('Enter the Denominator2: '))
    f2 = fractions.Fraction(num2, den2)
    operation = input('Enter the Required Operation (Add, Subtract, Multiply, Divide): ')
    result = 0
    if operation == 'Add' or 'add' or 'A' or 'a':
        result = f1.__add__(f2)
    elif operation == 'Subtract' or 'subtract' or 'S' or 's':
        result = f1.__sub__(f2)
    elif operation == 'Multiply' or 'multiply' or 'M' or 'm':
        result = f1.__mul__(f2)
    elif operation == 'Divide' or 'divide' or 'D' or 'd':
        result = f1.__divmod__(f2)
    print('The First Fraction is:', f1)
    print('The Second Fraction is:', f2)
    print('The Result of the Two Fractions After Making Operation on them:', result)


def ex_4():
    hs = input('Enter a Hyphened String: ')
    # for i in hs.split('-'):
    #     print(i)
    for i in hs:  # Emma-is-a-Data-Scientist
        if i == '-':
            print()
            continue
        print(i, end='')


def ex_5(sub, string):
    # return string.find(sub)
    x = string.find(sub)
    if x != -1:
        return True
    else:
        return False


def decimalToBinary(value):  # ex_6
    # b = bin(value)
    # print(b)

    x = value
    b = ''
    z = ''
    while value != 0:
        d = value // 2
        bit = value % 2
        if bit != 0:
            b += '1'
        elif bit == 0:
            b += '0'
        value = d
    for i in range(len(b) - 1, -1, -1):
        z += b[i]
    # print(b)
    print('The Binary Number of this Decimal Number (', x, '):', z)


def ex_7(sc, gs):
    for i in gs:
        if sc == i:
            continue
        print(i, end='')


def main():
    # ex_1()
    # fileName = input('Enter the File Name: ')
    # sumFile(fileName + '.txt')
    # ex_3()
    # ex_4()
    # sub = input('Enter the Sub string: ')
    # string = input('Enter the String: ')
    # if ex_5(sub, string):
    #     print('The First String IS a Substring of the Second String')
    # else:
    #     print('The First String IS Not a Substring of the Second String')
    # d = int(input('Enter a Decimal Integer Value: '))
    # decimalToBinary(d)
    sc = input('Enter a Specified Character: ')
    gs = input('Enter a Given String: ')
    ex_7(sc, gs)


main()
