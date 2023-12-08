# Exercise (11) :-

# def ex_1(n):
#     for i in range(n + 1):
#         for j in range(n + 1):
#             if i * j == n:
#                 yield i, j


def ex_1(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


def ex_2(n):  # Fibonacci Sequence: 0,1,1,2,3,5,8,13,...
    f, s = 0, 1
    for i in range(n + 1):
        yield f
        f, s = s, f + s


def main():
    x = int(input('Enter the Integer: '))
    print(f'The Factors OF ({x}) Are: ', end='')
    for i in ex_1(x):
        print(i, end=' ')

    # y = int(input('Enter the Number of the Terms of the Fibonacci Sequence: '))
    # print(f'The First ({y}) Terms of the Fibonacci Sequence: ', end='')
    # for i in ex_2(y):
    #     print(i, end=' ')


main()
