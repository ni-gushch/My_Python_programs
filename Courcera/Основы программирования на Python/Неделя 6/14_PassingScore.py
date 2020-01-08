class Pupil:
    Name = []
    fSub = 0
    sSub = 0
    tSub = 0
    sumFor3 = 0


infile = open("input.txt", "r", encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf8')
allPupilsList = infile.readlines()
K = int(allPupilsList[0])
successPA = []
for pupil in allPupilsList[1:]:
    temp = pupil.split()
    lenTemp = len(temp)
    cond1 = int(temp[lenTemp - 3]) >= 40
    cond2 = int(temp[lenTemp - 2]) >= 40
    cond3 = int(temp[lenTemp - 1]) >= 40
    if cond1 and cond2 and cond3:
        p = Pupil()
        p.Name = temp[:lenTemp - 3]
        p.fSub = int(temp[lenTemp - 3])
        p.sSub = int(temp[lenTemp - 2])
        p.tSub = int(temp[lenTemp - 1])
        p.sumFor3 = p.fSub + p.sSub + p.tSub
        successPA.append(p)
successPA.sort(key=lambda x: x.sumFor3, reverse=True)
if len(successPA) <= K:
    print(0, file=outFile)
elif successPA[0].sumFor3 == successPA[K].sumFor3:
    print(1, file=outFile)
else:
    while successPA[K - 1].sumFor3 == successPA[K].sumFor3:
        K -= 1
    print(successPA[K - 1].sumFor3, file=outFile)
infile.close()
outFile.close()
