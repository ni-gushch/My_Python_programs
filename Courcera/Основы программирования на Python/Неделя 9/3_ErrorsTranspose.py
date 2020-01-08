from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, listOfList=list(list())):
        lenList = len(listOfList[0])
        for l in listOfList:
            if len(l) != lenList or len(l) == 0:
                break
            if not str(l).isdigit:
                break
        self.matrix = copy.deepcopy(listOfList)
        self.rows = len(self.matrix)
        self.cols = lenList

    def __str__(self):
        resultStr = ''
        for i in self.matrix:
            resultStr += "\t".join(map(str, i))
            resultStr += "\n"
        return resultStr.strip()

    def size(self):
        return self.rows, self.cols

    def __add__(self, m):
        mSize = m.size()
        if self.size() == mSize:
            for i in range(mSize[0]):
                for j in range(mSize[1]):
                    m.matrix[i][j] += self.matrix[i][j]
            return m
        else:
            raise MatrixError(self, m)

    def __mul__(self, k=0.0):
        nM = copy.deepcopy(self)
        for i in range(len(nM.matrix)):
            for j in range(len(nM.matrix[i])):
                nM.matrix[i][j] *= k
        return nM

    __rmul__ = __mul__

    def transpose(self):
        tL = list()
        for i in range(self.cols):
            temp = list()
            for j in range(self.rows):
                temp.append(self.matrix[j][i])
            tL.append(temp)
        tempM = Matrix(tL)
        self.matrix = tempM.matrix
        self.rows = tempM.rows
        self.cols = tempM.cols
        return self

    @staticmethod
    def transposed(m):
        tL = list()
        for i in range(m.cols):
            temp = list()
            for j in range(m.rows):
                temp.append(m.matrix[j][i])
            tL.append(temp)
        return Matrix(tL)

exec(stdin.read())
