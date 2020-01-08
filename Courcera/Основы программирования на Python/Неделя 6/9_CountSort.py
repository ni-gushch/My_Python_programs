def CountSort(A):
    B = []
    cnt = [0] * 101
    for num in A:
        cnt[num] += 1
    for nowNum in range(101):
        if(cnt[nowNum] != 0):
            for i in range(cnt[nowNum]):
                B.append(nowNum)
    return B


inList = list(map(int, input().split()))
outList = CountSort(inList)
print(*outList)
