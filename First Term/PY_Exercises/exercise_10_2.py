# Exercise (10_2) :-

import abc
import math


class GeometricObject(abc.ABC):  # ex_2

    # def __init__(self, color, filled):
    #     self.color = color
    #     self.filled = filled

    color = 'Yellow'
    filled = True

    @abc.abstractmethod
    def getColor(self):
        pass

    @abc.abstractmethod
    def getFilled(self):
        pass

    @abc.abstractmethod
    def getArea(self):
        pass

    @abc.abstractmethod
    def getPerimeter(self):
        pass


class Triangle(GeometricObject):

    def __init__(self, color, filled, side1=1.0, side2=1.0, side3=1.0):
        # GeometricObject.color = color
        # GeometricObject.filled = filled
        super().__init__(color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getColor(self):
        return self.color

    def getFilled(self):
        return self.filled

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f'The Triangle\'s Color is: {self.getColor()}\nIs the Triangle Filled OR Not?: {self.getFilled()}' + \
               f'\nThe 3 Sides of the Triangle Are: {self.side1} , {self.side2} , {self.side3}' + \
               f'\nThe Area of the Triangle is: {self.getArea()}' + \
               f'\nThe Perimeter of the Triangle is: {self.getPerimeter()}'


def main():
    t = Triangle('Yellow', True, 1, 1.5, 1)
    print(t)


main()
