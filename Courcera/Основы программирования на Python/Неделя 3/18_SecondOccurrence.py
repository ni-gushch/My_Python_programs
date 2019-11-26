inputString = input()
firstH = inputString.find('f')
if firstH == -1:
    print("-2")
else:
    stringAfterH = inputString[firstH + 1:]
    secondH = stringAfterH.find('f')
    if secondH == -1:
        print('-1')
    else:
        print(firstH + secondH + 1)
