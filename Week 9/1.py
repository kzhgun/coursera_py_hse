from sys import stdin


class Matrix:
    def __init__(self, matrix):
        self.matrix = tuple(map(lambda x: tuple(x), matrix))

    def __str__(self):
        sinner = map(lambda x: '\t'.join(map(str, x)), self.matrix)
        s = '\n'.join(sinner)
        return s

    def size(self):
        t = (len(self.matrix), len(self.matrix[0]))
        return t


exec(stdin.read())
