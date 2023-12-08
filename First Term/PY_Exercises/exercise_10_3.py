# Exercise (10_3) :-

class Person:  # ex_3

    def __init__(self, name, address, phoneNumber, emailAddress):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

    def __str__(self):
        return f'The Class Name is: (Person)\nIts Data: ' \
               f'{self.name, self.address, self.phoneNumber, self.emailAddress}'


class Student(Person):

    def __init__(self, name, address, phoneNumber, emailAddress, classStatus):
        super().__init__(name, address, phoneNumber, emailAddress)
        self.classStatus = classStatus

    def __str__(self):
        return f'The Class Name is: (Student)\nIts Data: ' \
               f'{self.name, self.address, self.phoneNumber, self.emailAddress, self.classStatus}'


class Employee(Person):

    def __init__(self, name, address, phoneNumber, emailAddress, salary, dateHired):
        super().__init__(name, address, phoneNumber, emailAddress)
        self.salary = salary
        self.dateHired = dateHired

    def __str__(self):
        return f'The Class Name is: (Employee)\nIts Data: ' \
               f'{self.name, self.address, self.phoneNumber, self.emailAddress, self.salary, self.dateHired}'


class MyDate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.year, self.month, self.day}'


class Faculty(Employee):

    def __init__(self, name, address, phoneNumber, emailAddress, salary, dateHired, officeHours, rank):
        super().__init__(name, address, phoneNumber, emailAddress, salary, dateHired)
        self.officeHours = officeHours
        self.rank = rank

    def __str__(self):
        return f'The Class Name is: (Faculty)\nIts Data: ' \
               f'{self.name, self.address, self.phoneNumber, self.emailAddress, self.salary, self.dateHired, self.officeHours, self.rank}'


class Staff(Employee):

    def __init__(self, name, address, phoneNumber, emailAddress, salary, dateHired, title):
        super().__init__(name, address, phoneNumber, emailAddress, salary, dateHired)
        self.title = title

    def __str__(self):
        return f'The Class Name is: (Staff)\nIts Data: ' \
               f'{self.name, self.address, self.phoneNumber, self.emailAddress, self.salary, self.dateHired, self.title}'


def main():
    name = input('Enter your Name: ')
    address = input('Enter your Address: ')
    phoneNumber = int(input('Enter your Phone Number: '))
    emailAddress = input('Enter your Email Address: ')

    classStatus = input('Enter your Class Status (Freshman, Sophomore, Junior, Senior): ')

    salary = float(input('Enter your Salary: '))
    y = int(input('Enter Year: '))
    m = int(input('Enter Month: '))
    d = int(input('Enter Day: '))
    dateHired = MyDate(y, m, d)

    officeHours = int(input('Enter your Office Hours: '))
    rank = input('Enter your Rank: ')

    title = input('Enter your Title: ')

    p = Person(name, address, phoneNumber, emailAddress)
    su = Student(name, address, phoneNumber, emailAddress, classStatus)
    e = Employee(name, address, phoneNumber, emailAddress, salary, dateHired.__str__())
    f = Faculty(name, address, phoneNumber, emailAddress, salary, dateHired.__str__(), officeHours, rank)
    sa = Staff(name, address, phoneNumber, emailAddress, salary, dateHired.__str__(), title)

    print()
    print(p)
    print(su)
    print(e)
    print(dateHired)
    print(f)
    print(sa)


main()
