inputString = input()
firstH = inputString.find('h')
lastH = len(inputString) - inputString[::-1].find('h') - 1
print(inputString[0:firstH], inputString[lastH + 1:], sep='')
