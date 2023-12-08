# Exercise (9_3) :-

class Course:   # ex_3

    def __init__(self, courseName, students=None, numberOfStudents=0):
        if students is None:
            students = []
        self.__courseName = courseName
        self.__students = students
        self.__numberOfStudents = numberOfStudents

    def course(self, courseName):
        self.__courseName = courseName

    def getCourseName(self):
        return self.__courseName

    def addStudent(self, student):
        self.__students.append(student)
        self.__numberOfStudents += 1

    def dropStudent(self, student):
        self.__students.remove(student)
        if self.__numberOfStudents > 0:
            self.__numberOfStudents -= 1

    def getStudents(self):
        return self.__students

    def getNumberOfStudents(self):
        return self.__numberOfStudents


def main():
    c1 = Course('Course-(1)')

    c1.course('Python')

    c1.addStudent('Loay')
    c1.addStudent('Sohyla')
    c1.addStudent('Eyad')

    print('The Course Name:', c1.getCourseName())
    print('The Students In This Course:', c1.getStudents())
    for i in range(len(c1.getStudents())):
        print(c1.getStudents()[i], end=' , ')
    print()
    print('The Number Of Students In This Course:', c1.getNumberOfStudents())

    c1.dropStudent('Sohyla')

    print('The Course Name:', c1.getCourseName())
    print('The (NEW) Students In This Course:', c1.getStudents())
    for i in range(len(c1.getStudents())):
        print(c1.getStudents()[i], end=' , ')
    print()
    print('The (NEW) Number Of Students In This Course:', c1.getNumberOfStudents())


main()
