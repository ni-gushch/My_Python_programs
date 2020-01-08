class Pupil:
    Name = ''
    Class = 0
    Score = 0

inFile = open('input.txt', 'r', encoding='utf-8')
listPupils9 = list()
listPupils10 = list()
listPupils11 = list()
for line in inFile.readlines():
    tempPupil = Pupil()
    lineSplit = line.split()
    tempPupil.Name = lineSplit[0] + lineSplit[1]
    tempPupil.Class = int(lineSplit[2])
    tempPupil.Score = int(lineSplit[3])
    if tempPupil.Class == 9:
        listPupils9.append(tempPupil)
    elif tempPupil.Class == 10:
        listPupils10.append(tempPupil)
    elif tempPupil.Class == 11:
        listPupils11.append(tempPupil)
listPupils9.sort(key=lambda x: x.Score, reverse=True)
listPupils10.sort(key=lambda x: x.Score, reverse=True)
listPupils11.sort(key=lambda x: x.Score, reverse=True)
k9, k10, k11 = 0, 0, 0
for item9 in listPupils9:
    if item9.Score == listPupils9[0].Score:
        k9 += 1
    else:
        break
for item10 in listPupils10:
    if item10.Score == listPupils10[0].Score:
        k10 += 1
    else:
        break
for item11 in listPupils11:
    if item11.Score == listPupils11[0].Score:
        k11 += 1
    else:
        break
print(k9, k10, k11)
inFile.close()
