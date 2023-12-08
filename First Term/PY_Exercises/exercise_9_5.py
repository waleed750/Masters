# Exercise (9_5) :-

class Account:   # ex_5

    def __init__(self, name, account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError('Not Enough Balance In You Account')

    def get(self):
        return self.__name, self.__account_number, self.__balance


def main():
    a1 = Account('LOAY HATEM', 3, 3000)
    print('The Data OF My Account is:', a1.get())

    a1.deposit(1200)
    print('The Data OF My Account is:', a1.get())

    a1.withdraw(400)
    print('The Data OF My Account is:', a1.get())


main()
