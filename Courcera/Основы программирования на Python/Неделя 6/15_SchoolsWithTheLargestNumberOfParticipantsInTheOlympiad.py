inFile = open('input.txt', 'r', encoding='utf-8')
line = inFile.readline()
numPups = [0] * 99
while line != '':
    itemsInLine = line.split()
    numPups[int(itemsInLine[2]) - 1] += 1
    line = inFile.readline()
m = numPups[0]
scList = list()
for i in range(1, 99):
    if numPups[i] > m:
        scList.clear()
        scList.append(i + 1)
        m = numPups[i]
    elif numPups[i] == m:
        scList.append(i + 1)
print(*scList)
inFile.close()
