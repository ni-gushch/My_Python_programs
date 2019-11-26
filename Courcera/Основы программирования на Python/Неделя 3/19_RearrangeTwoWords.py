inputString = input()
space = inputString.find(' ')
print(inputString[space + 1:], inputString[:space])
