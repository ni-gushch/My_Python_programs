pupilsCount = int(input())
allLang = set()
allPupilsKnew = set()
for i in range(pupilsCount):
    langCount = int(input())
    tempSet = set()
    for j in range(langCount):
        tempLang = input()
        allLang.add(tempLang)
        tempSet.add(tempLang)
    if i == 0:
        allPupilsKnew = tempSet.copy()
    else:
        allPupilsKnew &= tempSet
print(len(allPupilsKnew))
for i in allPupilsKnew:
    print(i)
print(len(allLang))
for i in allLang:
    print(i)
