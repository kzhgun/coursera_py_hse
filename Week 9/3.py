from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


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

    def __add__(self, other):
        res = []
        if len(self.matrix) == len(other.matrix):
            def mysumm(a, b):
                return a + b

            for i in range(self.size()[0]):
                res.append(list(map(mysumm, self.matrix[i], other.matrix[i])))
            return Matrix(res)
        else:
            raise MatrixError(self, other)

    def __mul__(self, digit=0):
        res = []
        for i in range(self.size()[0]):
            res.append(list(map(lambda a: a * digit, self.matrix[i])))
        return Matrix(res)

    def transpose(self):
        t_matrix = list(zip(*self.matrix))
        self.matrix = t_matrix
        return Matrix(t_matrix)

    def transposed(self):
        m8 = list(zip(*self.matrix))
        return Matrix(m8)
    __rmul__ = __mul__


exec(stdin.read())
