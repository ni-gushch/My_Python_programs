l = list(map(int, input().split()))
C = list(map(int, input().split()))
l.append(C[1])
for i in range(len(l) - 1, C[0], -1):
    l[i], l[i - 1] = l[i - 1], l[i]
print(*l)
