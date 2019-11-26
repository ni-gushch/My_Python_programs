inputString = input()
reversedString = inputString[::-1]
firstF = inputString.find('f')
lastF = -1
if reversedString.find('f') != -1:
    lastF = len(inputString) - reversedString.find('f') - 1
if firstF == -1 and lastF == -1:
    print()
elif firstF == lastF:
    print(firstF)
else:
    print(firstF, lastF)
