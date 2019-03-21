from operator import itemgetter

class School(object):
    def __init__(self):
        self.__students = []

    def add_student(self, name, grade):
        self.__students.append((name, grade))

    def roster(self):
        self.__students.sort(key=itemgetter(1,0))
        return [student[0] for student in self.__students]

    def grade(self, grade_number):
        self.__students.sort(key=itemgetter(1,0))
        return [student[0] for student in self.__students if student[1] == grade_number]
