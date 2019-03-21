class Garden(object):
    def __init__(self, diagram, students="Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry"):
        self.students = students.split(" ").sort()
        self.garden = diagram.split("\n")

    def plants(self, student):
        i = self.students.index(student)
        print(self.garden[0][i:i+1].join(", ") + ", " + self.garden[1][i:i+1].join(", "))
        return self.garden[0][i:i+1].join(", ") + ", " + self.garden[1][i:i+1].join(", ")
