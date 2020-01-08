s = int(input())
sList = list(map(int, input().split()))
sList.sort()
k = 0
q = 0
for shoes in sList:
    if shoes == s and q == 0:
        k += 1
        q = 1
    elif shoes >= s + 3:
        k += 1
        s = shoes
        q = 1
print(k)
