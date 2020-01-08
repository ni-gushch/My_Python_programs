l = list(map(int, input().split()))
length = len(l)
for i in range(0, length - 1):
    if (l[i] > 0 and l[i + 1] > 0) or (l[i] < 0 and l[i + 1] < 0):
        print(l[i], l[i + 1])
        break
