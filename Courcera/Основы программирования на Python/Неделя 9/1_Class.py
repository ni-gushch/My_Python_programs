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
        self.listOfLists = copy.deepcopy(listOfList)
        self.rows = len(self.listOfLists)
        self.cols = lenList

    def __str__(self):
        resultStr = ''
        for i in self.listOfLists:
            resultStr += "\t".join(map(str, i))
            resultStr += "\n"
        return resultStr.strip()

    def size(self):
        return self.rows, self.cols

exec(stdin.read())
