inFile = open("16_input.txt", 'r', encoding='utf-8')
line = inFile.readline()
sList9 = list()
sList10 = list()
sList11 = list()
while line != '':
    temp = line.split()
    if int(temp[2]) == 9:
        sList9.append(int(temp[3]))
    elif int(temp[2]) == 10:
        sList10.append(int(temp[3]))
    elif int(temp[2]) == 11:
        sList11.append(int(temp[3]))
    line = inFile.readline()
sList9.sort()
sList10.sort()
sList11.sort()
max9 = sList9[-1]
max10 = sList10[-1]
max11 = sList11[-1]
while max9 == sList9[-1]:
    sList9.pop()
while max10 == sList10[-1]:
    sList10.pop()
while max11 == sList11[-1]:
    sList11.pop()
print(sList9[-1], sList10[-1], sList11[-1])
inFile.close()
