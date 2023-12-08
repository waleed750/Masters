# Exercise (4) :-

import math
import random


def fun1(i, num):  # ex_1()
    for j in range(1, i + 1):
        print(num, end=" ")
        num *= 2
    print()


def sumDigits(n):  # ex_2()
    s = 0
    for i in str(n):
        s += int(i)
    print('The Sum of these Digits are:', s)


def printChars(ch1, ch2, numberPerLine):  # ex_3()
    count = 0
    for i in range(ord(ch1), ord(ch2) + 1):
        print(chr(i), end=' ')
        count += 1
        if count % numberPerLine == 0:
            print()


def isValid(side1, side2, side3):  # ex_4()
    if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:
        return True
    else:
        return False


def area(side1, side2, side3):
    if isValid(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        a = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        print('The Area of this Triangle is:', a)
    else:
        print('The Input is InValid')


def printMatrix(n):  # ex_5()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(random.choice((0, 1)), end=' ')
        print()


def roll():  # ex_6()
    return random.randint(1, 6)


# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
def play():
    # First Die Rolling :-
    x = roll()
    # Second Die Rolling :-
    y = roll()
    s = x + y

    if s == 2 or s == 3 or s == 12:
        print('Craps, You Lose!')
    elif s == 7 or s == 11:
        print('Natural, You Win!')
    else:  # 4, 5, 6, 8, 9 or 10
        print('A Point is Established')
        while s in (4, 5, 6, 8, 9, 10):
            x = roll()
            y = roll()
            s = x + y
            if s == 7:
                print('Craps, You Lose!')


def main():
    # i = 1
    # while i <= 6:
    #     fun1(i, 2)
    #     i += 1
    # sumDigits(234)
    # printChars('A', 'Z', 10)
    # side1 = int(input('Enter the First Side of the Triangle: '))
    # side2 = int(input('Enter the Second Side of the Triangle: '))
    # side3 = int(input('Enter the Third Side of the Triangle: '))
    # area(side1, side2, side3)
    # printMatrix(3)
    play()


main()
