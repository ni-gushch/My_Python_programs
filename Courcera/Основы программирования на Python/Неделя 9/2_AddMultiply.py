from sys import stdin
import copy


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

    def __mul__(self, k=0.0):
        nM = copy.deepcopy(self)
        for i in range(len(nM.matrix)):
            for j in range(len(nM.matrix[i])):
                nM.matrix[i][j] *= k
        return nM

    __rmul__ = __mul__


exec(stdin.read())
