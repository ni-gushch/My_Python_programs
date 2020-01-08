l = list(map(int, input().split()))
k = []
j = 0
for i in l:
    if i != 0:
        k.append(i)
    else:
        j += 1
for m in range(j):
    k.append(0)
l = k
print(*l)
