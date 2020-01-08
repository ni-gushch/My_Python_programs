n = int(input())
allTuple = tuple(range(1, n + 1))
inT = tuple()
for i in range(1, n):
    a = int(input())
    inT += (a,)
for i in allTuple:
    k = 0
    for j in inT:
        if int(i) == int(j):
            k += 1
    if k == 0:
        print(int(i))
        break
