distList = list(map(int, input().split()))
costList = list(map(int, input().split()))
distList.sort()
costList.sort(reverse=True)
sumCost = 0
for i in range(len(distList)):
    sumCost += distList[i] * costList[i]
print(sumCost)
