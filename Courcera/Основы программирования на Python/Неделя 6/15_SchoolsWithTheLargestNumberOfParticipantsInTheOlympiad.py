inFile = open('input.txt', 'r', encoding='utf-8')


class Pupils:
    def __init__(self, classNum, pupilCount):
        self.classNum = classNum
        self.pupilCount = pupilCount


def firstOrNone(list, filter):
    for x in list:
        if filter(x):
            return x
    return None


line = inFile.readline()
pupilsList = []
while line != '':
    itemsInLine = line.split()
    classNumber = int(itemsInLine[2])
    a = firstOrNone(pupilsList, lambda x: x.classNum == classNumber)
    if a is not None:
        a.pupilCount += 1
    else:
        pupilsList.append(Pupils(classNumber, 1))
    line = inFile.readline()
pupilsList.sort(key=lambda k: k.pupilCount, reverse=True)
resultClasses = [pupilsList[0].classNum]
maxCount = pupilsList[0].pupilCount
for i in range(1, len(pupilsList)):
    if pupilsList[i].pupilCount == maxCount:
        resultClasses.append(pupilsList[i].classNum)
    else:
        break
resultClasses.sort()
print(*resultClasses)
inFile.close()
