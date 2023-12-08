# Exercise (9_4) :-

import math


class Circle:  # ex_4

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError('Negative radius')
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__radius

    def getArea(self):
        return math.pi * self.__radius * self.__radius

    def getPerimeter(self):
        return 2 * math.pi * self.__radius

    def contains1(self, x, y):
        d = math.sqrt((y - self.__y) ** 2 + (x - self.__x) ** 2)
        if d < self.__radius:
            return True
        else:
            return False

    def contains2(self, c):
        d = math.sqrt((c.getY() - self.__y) ** 2 + (c.getX() - self.__x) ** 2)
        if d + c.getRadius() < self.__radius:
            return True
        else:
            return False

    def overlaps(self, c):
        d = math.sqrt((c.getY() - self.__y) ** 2 + (c.getX() - self.__x) ** 2)
        if d + c.getRadius() == self.__radius:
            return True
        else:
            return False


def main():
    c1 = Circle(2, 2, 5.5)  # Is Equivalent TO ==> Circle.contains1(c1, 3, 3)

    print('The Area of the Circle:', c1.getArea())
    print('The Perimeter of the Circle:', c1.getPerimeter())
    print('The Result of the (Contains1) Circle:', c1.contains1(3, 3))
    print('The Result of the (Contains2) Circle:', c1.contains2(Circle(4, 5, 10.5)))
    print('The Result of the (Overlaps) Circle:', c1.overlaps(Circle(3, 5, 2.3)))


main()
