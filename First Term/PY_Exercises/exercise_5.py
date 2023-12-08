# Exercise (5) :-

import math
import random
import time


def ex_1_2_3():
    count = 1
    x = random.randrange(1, 101)
    print(x)
    u = int(input('Enter an Integer Number: '))
    start = time.perf_counter()
    while u != x:
        count += 1
        print("Computer's FeedBack :- ", end='')
        if u > x:
            print('!Too High!')
        else:
            print('!Too Low!')
        u = int(input('Again, Enter an Integer Number: '))
    else:
        end = time.perf_counter()
        elapsedTime = end - start
        print('The Elapsed Time of Guesses is:', elapsedTime)
        print('The Number of Guesses is:', count)
        print('!Excellent Guess!')


def ex_4():
    x = math.pi
    fx = math.cos(2 * x)
    fxd = -(2 * math.sin(2 * x))
    fxdd = -(4 * math.cos(2 * x))
    return x, fx, fxd, fxdd


def circle_area(r):  # ex_5()
    ca = math.pi * r * r
    return ca


def cylinder_surface_area(h, r):
    ba = circle_area(r)
    sa = 2 * math.pi * r * h
    csa = 2 * ba + sa
    return csa


def singleLetterCount(w, l):  # ex_6()
    count = 0
    st = ''
    for i in w:
        if l == i.upper() or l == i.lower():
            count += 1
            st += i
    return count, st


def main():
    # ex_1_2_3()
    # x, y, a, b = ex_4()
    # print('The Value of PI is:', x)
    # print('The Result of f(x) is:', y)
    # print('The Result of f\'(x) is:', a)
    # print('The Result of f\'\'(x) is:', b)
    # r = float(input('Enter the Radius of the Circle: '))
    # print('The Area of the Circle is:', circle_area(r))
    # h = float(input('Enter the Height of the Cylinder: '))
    # br = float(input('Enter the Base Radius of the Cylinder: '))
    # print('The Area of the Cylinder is:', cylinder_surface_area(h, br))
    w = input('Enter the Word: ')
    l = input('Enter the Letter: ')
    x, y = singleLetterCount(w, l)
    if x == 0:
        print('The Letter (' + l + ') Not Found in (' + w + ').')
    else:
        print('The Number of Times the Letter (' + l + ') Appears in the Word (' + w + ') is:', x, y)


main()
