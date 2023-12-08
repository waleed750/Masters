# Exercise (9_1) :-

class MyInteger:    # ex_1

    def __init__(self, value):
        self.__value = value

    def get(self):
        return self.__value

    def isEven(self):
        if self.__value % 2 == 0:
            return True
        else:
            return False

    def isOdd(self):
        if self.__value % 2 != 0:
            return True
        else:
            return False

    def isPrime(self):
        if self.__value >= 2:
            if self.__value == 2 or self.__value % 2 != 0:
                return True
            else:
                return False
        else:
            return False

    def equals(self, m, v):
        if m.get() == v:
            return True
        else:
            return False


def main():
    m = int(input('Enter an Integer Value: '))
    myint = MyInteger(m)    # Is Equivalent TO MyInteger.get(myint)
    print('The Integer Value is:', myint.get())
    print('Is the Value Even?:', myint.isEven())
    print('Is the Value Odd?:', myint.isOdd())
    print('Is the Value Prime?:', myint.isPrime())

    v = int(input('Enter the Value You Want to Compare Equality With: '))
    print('Is the Two Value Equals?:', myint.equals(myint, v))


main()
