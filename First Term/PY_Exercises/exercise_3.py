# Exercise (3) :-

def ex_1():
    i = int(input('Enter an UnSpecified Number of Integers: '))
    j = ''
    p, n = 0, 0
    s, a = 0, 0
    while i != 0:
        j += str(i)
        if i < 0:
            n += 1
            s += i
        elif i > 0:
            p += 1
            s += i
        i = int(input('Enter an UnSpecified Numbers of Integers: '))
    a = float(s / (n + p))
    print('\nThe UnSpecified Numbers of Integers:', j)
    print('The Sum of Integers:', s)
    print('The Average of Integers:', a)
    print('The Positive Count of Integers:', p)
    print('The Negative Count of Integers:', n)



# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
def ex_2():
    e = int(input('Enter the Number of Students: '))
    n = []
    s = []
    for i in range(0, e):
        n += [input('Enter Each Student Name: ')]
        s += [input('Enter Each Student Score: ')]
    print(n, s)
    print('The Name of the Student with the Highest Score is:', n[s.index(max(s))])
    print('The Highest Score of this Student is:', s[s.index(max(s))])


def ex_3():
    count = 0
    for j in range(2001, 2101):
        if j % 4 == 0 and j % 100 != 0 or j % 400 == 0:
            print(j, end=', ')
            count += 1
        if count == 10:
            print()
            count = 0


def ex_4():
    amount = int(input('Enter an Amount: '))  # $100
    air = int(input('Enter an Annual Interest Rate: '))  # 5%
    nom = int(input('Enter the Number of Months: '))  # 6 Months
    mir = (air / 100) / nom  # Monthly Interest Rate
    for i in range(1, nom + 1):
        amount = amount * (1 + mir)
        print(amount)
    print('The Amount in the Savings Account after the Given Month', amount)


def ex_5():
    # d = int(input('Enter a Decimal Integer: '))
    # b = bin(d)
    # print(b)

    d = int(input('Enter a Decimal Integer: '))
    x = d
    b = ''
    z = ''
    while d != 0:
        d1 = d // 2
        bit = d % 2
        if bit != 0:
            b += '1'
        elif bit == 0:
            b += '0'
        d = d1
    for i in range(len(b) - 1, -1, -1):
        z += b[i]
    # print(b)
    print('The Binary Number of this Decimal Number (', x, '):', z)


def main():
    # ex_1()
    # ex_2()
    # ex_3()
    # ex_4()
    ex_5()


main()
