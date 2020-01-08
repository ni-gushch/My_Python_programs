class Pupil:
    fName = ''
    lName = ''
    cl = 0
    score = 0


listPupils = []
inFile = open('input.txt', 'r', encoding='utf8')
for p in inFile:
    tempData = p.split()
    tempPupil = Pupil()
    tempPupil.fName = tempData[0]
    tempPupil.lName = tempData[1]
    tempPupil.cl = int(tempData[2])
    tempPupil.score = int(tempData[3])
    listPupils.append(tempPupil)
grade9 = []
sumG9 = 0
grade10 = []
sumG10 = 0
grade11 = []
sumG11 = 0
for i in listPupils:
    if i.cl == 9:
        grade9.append(i)
        sumG9 += i.score
    elif i.cl == 10:
        grade10.append(i)
        sumG10 += i.score
    elif i.cl == 11:
        grade11.append(i)
        sumG11 += i.score
avG9 = sumG9 / len(grade9)
avG10 = sumG10 / len(grade10)
avG11 = sumG11 / len(grade11)
print('{0:.6f}'.format(avG9), '{0:.6f}'.format(avG10), '{0:.6f}'.format(avG11))
