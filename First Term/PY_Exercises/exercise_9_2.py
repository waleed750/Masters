# Exercise (9_2) :-

import math


class MyPoint:  # ex_2

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance1(self, mp):
        return math.sqrt((mp.getX() - self.__x) ** 2 + (mp.getY() - self.__y) ** 2)

    def distance2(self, x, y):
        return math.sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)

    def __str__(self):
        return f'({self.__x},{self.__y})'


def main():
    mypoint1 = MyPoint(0, 0)
    mypoint2 = MyPoint(10, 30.5)

    print('The Value of (X1):', mypoint1.getX())
    print('The Value of (Y1):', mypoint1.getY())
    print('The Values of (X1,Y1):', mypoint1)

    print('The Value of (X2):', mypoint2.getX())
    print('The Value of (Y2):', mypoint2.getY())
    print('The Values of (X2,Y2):', mypoint2)

    print('The Distance Between (X1,Y1) And (X2,Y2):', mypoint1.distance1(mypoint2))

    x = float(input('Enter the Value of (X2): '))
    y = float(input('Enter the Value of (Y2): '))
    print('The Distance Between (X1,Y1) And Specified (X2,Y2):', mypoint1.distance2(x, y))


main()
