# Exercise (8) :-

def sum_positive(a):  # ex_1
    s = 0
    for i in a:
        if i > 0:
            s += i
    return s


def count_evens(a):  # ex_2
    c = 0
    for i in a:
        if i % 2 == 0:
            c += 1
    return c


def reverse(lst):  # ex_3
    lst2 = []
    lst3 = []
    for i in range(len(lst) - 1, -1, -1):
        lst2.append(lst[i])
    print('The Reversed List is:', lst2)
    while lst2:
        lw = lst2[0]
        for i in lst2:
            if i < lw:
                lw = i
        lst3.append(lw)
        lst2.remove(lw)
    print('The Reversed & Rearranged List is:', lst3)


def ex_4():
    l1 = [x + 1 for x in [2, 4, 6, 8]]
    l2 = [10 * x for x in range(5, 10)]
    l3 = [x for x in range(10, 21) if x % 3 == 0]
    l4 = [(x, y) for x in range(3) for y in range(4)]
    l5 = [(x, y) for x in range(3) for y in range(4) if (x + y) % 2 == 0]
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)


def ex_5():
    l1 = [x ** 2 for x in range(1, 6)]
    l2 = [x / 4.0 for x in range(1, 7)]
    l3 = [(x, y) for x in ('a', 'b') for y in range(3)]
    print(l1)
    print(l2)
    print(l3)


def ex_6():
    lst = [[2, 4, 3, 4, 5, 8, 8],
           [7, 3, 4, 3, 3, 4, 4],
           [3, 3, 4, 3, 3, 2, 2],
           [9, 3, 4, 7, 3, 4, 1],
           [3, 5, 4, 3, 6, 3, 8]]

    t = 0
    c = 1
    print('                 Su  M  T  W  H  F  Sa')
    for i in lst:
        print('Employee (', c, ') :', end='  ')
        for j in i:
            print(j, end='  ')
            t += j
        print(f',  The Total Hours of Employee ({c}) Are:', t)
        c += 1


def ex_7():
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lst1)
    lst2 = []
    for i in range(1, 11):
        lst2 += [i]
    print(lst2)
    lst3 = list(range(1, 11))
    print(lst3)
    lst4 = [i for i in range(1, 11)]
    print(lst4)
    s5 = '1 2 3 4 5 6 7 8 9 10'
    lst5 = list(s5.split(' '))
    print(lst5)


def ex_8(st):
    # lst = []
    # for i in st.split(','):
    #     if not lst.__contains__(i):
    #         lst += [i]
    # print(lst)
    # lst.sort()
    # print(lst)

    lst = []
    lst2 = []
    lst3 = []
    for i in st.split(','):
        if not lst.__contains__(i):
            lst += [i]
    print(lst)
    for i in lst:
        # lst3 += [ord(i)]
        lst3 += [ord(i[0])]
    print(lst3)
    while lst3:
        lw = lst3[0]
        for i in lst3:
            if i < lw:
                lw = i
        for i in lst:
            if i[0] == chr(lw):
                lst2.append(i)
                lst3.remove(lw)
    print(lst2)


def main():
    # lst = [3, -3, 5, 2, -1, 2]
    # print('The Sum of the Positive Values:', sum_positive(lst))
    # lst = [3, 5, 4, -1, 0]
    # print('The Count of the Evens Values:', count_evens(lst))
    lst = [2, 3, 4, 7, 8, 0]
    print('The Original List is:', lst)
    reverse(lst)
    # ex_4()
    # ex_5()
    # ex_6()
    # ex_7()
    # s = input('Enter a Comma Separated Sequence of Words: ')
    # ex_8(s)


main()
