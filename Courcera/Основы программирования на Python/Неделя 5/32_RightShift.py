l = list(map(int, input().split()))
k = [l[len(l) - 1], ]
for i in range(0, len(l) - 1):
    k.append(l[i])
l = k
print(*l)
