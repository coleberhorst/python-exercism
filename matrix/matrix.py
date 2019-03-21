class Matrix(object):
    def __init__(self, matrix_string):
        self.data = matrix_string.split("\n")
        for row in range(len(self.data)):
            self.data[row] = self.data[row].split(" ")
            self.data[row] = list(map(int, self.data[row]))
        print(self.data)

    def row(self, index):
        return self.data[index-1]

    def column(self, index):
        return [row[index-1] for row in self.data]
