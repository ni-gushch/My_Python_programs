def SortByDist(point):
    return point[0]


def SortByNum(point):
    return point[1]


townCount = int(input())
townDist = list(map(int, input().split()))
defCount = int(input())
defDist = list(map(int, input().split()))
for i in range(townCount):
    townDist[i] = [townDist[i], i]
for i in range(defCount):
    defDist[i] = [defDist[i], i]
townDist.sort(key=SortByDist)
defDist.sort(key=SortByDist)
CD = []
i = 0
j = 0
for _ in range(townCount):
    if j >= defCount:
        num = (townDist[i][1], defDist[j - 1][1] + 1)
        CD.append(num)
        i += 1
    elif townDist[i][0] == defDist[j][0]:
        num = (townDist[i][1], defDist[j][1] + 1)
        CD.append(num)
        i += 1
    elif townDist[i][0] > defDist[j][0]:
        while j < defCount and townDist[i][0] > defDist[j][0]:
            dif1 = townDist[i][0] - defDist[j][0]
            j += 1
        if j < defCount:
            dif2 = defDist[j][0] - townDist[i][0]
            if dif1 <= dif2:
                num = (townDist[i][1], defDist[j - 1][1] + 1)
                CD.append(num)
                j -= 1
            else:
                num = (townDist[i][1], defDist[j][1] + 1)
                CD.append(num)
        else:
            num = (townDist[i][1], defDist[j - 1][1] + 1)
            CD.append(num)
        i += 1
    else:
        num = (townDist[i][1], defDist[j][1] + 1)
        CD.append(num)
        i += 1
CD.sort()
numTown = 0
CD2 = []
while numTown < len(CD):
    numBunker = CD[numTown][1]
    CD2.append(numBunker)
    numTown += 1
print(*CD2)
