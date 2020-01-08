n = int(input())
sinonDict = {}
for i in range(n):
    tempInput = input().split()
    sinonDict[tempInput[1]] = tempInput[0]
    sinonDict[tempInput[0]] = tempInput[1]
print(sinonDict[input()])
