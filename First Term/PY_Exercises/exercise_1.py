# Exercise (1) :-

import math


def ex_1():
    r = float(input('Enter the Radius of the Cylinder: '))
    l = float(input('Enter the Length of the Cylinder: '))
    a = r * r * math.pi  # 3.14
    v = a * l
    return v


def ex_2():
    f = float(input('Enter a Number in Feet: '))
    m = f * 0.305
    return m


def ex_3():
    sub = float(input('Enter Subtotal ($): '))
    tip = float(input('Enter Tip Rate (%): '))
    ftip = (tip / 100) * sub
    total = sub + ftip
    return ftip, total


def ex_4():
    wp = float(input('Enter your Weight in Pounds: '))
    hi = float(input('Enter your Height in Inches: '))
    wk = wp * 0.45359237
    hm = hi * 0.0254
    bmi = wk / (hm * hm)
    return bmi


def ex_5():
    x1, y1 = float(input('Enter the X1: ')), float(input('Enter the Y1: '))
    x2, y2 = float(input('Enter the X2: ')), float(input('Enter the Y2: '))
    x3, y3 = float(input('Enter the X3: ')), float(input('Enter the Y3: '))
    s1 = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    s2 = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))
    s3 = math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
    s = (s1 + s2 + s3) / 2
    a = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
    return a


def ex_6():
    t = float(input('Enter the Time in Seconds: '))  # 1 Billion
    y = t // (365 * 4.3 * 7 * 24 * 60 * 60)           # 949,233,600 --- 31,207,680
    t %= (365 * 4.3 * 7 * 24 * 60 * 60)
    mn = t // (4.3 * 7 * 24 * 60 * 60)
    t %= (4.3 * 7 * 24 * 60 * 60)
    w = t // (7 * 24 * 60 * 60)
    t %= (7 * 24 * 60 * 60)
    d = t // (24 * 60 * 60)
    t %= (24 * 60 * 60)
    h = t // (60 * 60)
    t %= (60 * 60)
    m = t // 60
    t %= 60
    s = t
    print("y:mn:w:d:h:m:s-> %d:%d:%d:%d:%d:%d:%d" % (y, mn, w, d, h, m, s))
    # print(int(y), ':', int(mn), ':', int(w), ':', int(d), ':', int(h), ':', int(m), ':', int(s))


def ex_7():
    ascii = int(input('Enter the ASCII Code of any Character: '))
    if 0 <= ascii <= 128:  # ascii >= 0 and ascii <= 128
        e = chr(ascii)
        return e
    else:
        return None


def main():
    # print(math.pi)
    # print('The Volume of the Cylinder is:', ex_1())
    # print('The Number Converted into Meter is:', ex_2())
    # tip, total = ex_3()
    # print('The Tip Rate is: $', tip, '\nThe Total is: $', total)
    # print('The BMI of Your Weight & Height is:', ex_4())
    # print('The Area of this Triangle is:', ex_5())
    ex_6()
    # print('The ASCII Code of the Number you Entered is:', ex_7())


# ------------------------------------------------------------------------------------------------------------------
# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


main()
