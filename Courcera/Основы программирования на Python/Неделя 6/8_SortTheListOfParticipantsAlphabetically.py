class Pupil:
    lastName = ''
    firstName = ''
    schoolNum = 0
    score = 0


def sortByLastName(pupil):
    return pupil.lastName


infile = open("input.txt", "r", encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf8')
arr = []
lines = infile.readlines()
for i in lines:
    pupil = Pupil()
    line = i.split()
    pupil.lastName = line[0]
    pupil.firstName = line[1]
    pupil.schoolNum = line[2]
    pupil.score = line[3]
    arr.append(pupil)
arr.sort(key=sortByLastName)
for i in arr:
    print(i.lastName, i.firstName, i.score, file=outFile)
infile.close()
outFile.close()
