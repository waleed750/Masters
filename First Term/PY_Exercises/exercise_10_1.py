# Exercise (10_1) :-

class Account:  # ex_1

    def __init__(self, acctNo, balance):
        self.__acctNo = acctNo
        self.balance = balance

    def __str__(self):
        return f'The Account Number: {self.__acctNo} , The Balance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount


class Sav_Acct(Account):

    def __init__(self, acctNo, balance, rate):
        super().__init__(acctNo, balance)
        self.__rate = rate

    def compound(self):
        self.deposit(self.__rate / 100)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError('Not Enough Balance In You Account')

    def __str__(self):
        return 'The Type of This Account is: (Savings Account)\n' + \
               f'{Account.__str__(self)} , The Monthly Rate: {self.__rate}'


class Cur_Acct(Account):

    def __init__(self, acctNo, balance, charge):
        super().__init__(acctNo, balance)
        self.__charge = charge

    def cash_check(self, amount):
        check = self.balance - (amount + self.__charge)
        if check < self.balance:
            return check
        else:
            return 0

    def __str__(self):
        return 'The Type of This Account is: (Current Account)\n' + \
               f'{Account.__str__(self)} , The Charge: {self.__charge}'


def main():
    acctList = []

    for i in range(5):
        acctList.append(input('Enter the Account Type (Savings Account OR Current Account): '))

    for i in acctList:
        if i == 'Savings Account':
            an1 = int(input('Enter the Account Number: '))
            b1 = float(input('Enter the Account Balance: '))
            r = int(input('Enter the Account Monthly Rate: '))
            s = Sav_Acct(an1, b1, r)
            acctList.append(s)
        elif i == 'Current Account':
            an2 = int(input('Enter the Account Number: '))
            b2 = float(input('Enter the Account Balance: '))
            ch = int(input('Enter the Account Charge Check: '))
            c = Cur_Acct(an2, b2, ch)
            acctList.append(c)

    for i in acctList:
        print(i)


main()
