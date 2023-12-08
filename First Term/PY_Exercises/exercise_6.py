# Exercise (6) :-

import math


def mystery_1(a, b):  # ex_1()
    if b == 0:
        return 0
    else:
        return mystery_1(a, b - 1) + 2


def mystery_2(a, b):  # ex_1()
    if b == 0:
        return 1
    else:
        return mystery_2(a, b - 1) * 2


def sumInt(n):  # ex_2()
    if n == 0:
        return 0
    else:
        return n + sumInt(n - 1)


def ackerman(m, n):  # ex_3()
    if m == 0:
        return n + 1
    elif m != 0 and n == 0:
        return ackerman(m - 1, 1)
    elif m != 0 and n != 0:
        return ackerman(m - 1, ackerman(m, n - 1))


def gcd(num1, num2):  # ex_4()
    # Determine the smallest of num1 and num2
    min = num1 if num1 < num2 else num2
    # 1 definitely is a common factor to all ints
    largest_factor = 1
    for i in range(1, min + 1):
        if num1 % i == 0 and num2 % i == 0:
            largest_factor = i  # Found larger factor
    return largest_factor


def distance(x1, y1, x2, y2):  # ex_5()

    def diff(a, b):
        return a - b

    def square(z):
        return z * z

    return math.sqrt(square(diff(x1, x2)) * square(diff(y1, y2)))


def power_generator(num):  # ex_6()
    # Create the inner function
    def power_n(power):
        return num ** power

    return power_n


def main():
    # print(mystery_1(2, 5))
    # print(mystery_2(2, 5))
    # print(sumInt(10))
    # print(ackerman(2, 10))
    # Prompt user for input
    # num1 = int(input('Please enter an integer: '))
    # num2 = int(input('Please enter another integer: '))
    # # Call the function gcd and print the returned GCD
    # print("GCD of", num1, "and", num2, "is", gcd(num1, num2))
    # x1 = int(input('Enter the X1: '))
    # y1 = int(input('Enter the Y1: '))
    # x2 = int(input('Enter the X2: '))
    # y2 = int(input('Enter the Y2: '))
    # print('The Distance is:', distance(x1, y1, x2, y2))
    power_two = power_generator(2)
    power_three = power_generator(3)
    print(power_two(8))
    print(power_three(4))


main()
