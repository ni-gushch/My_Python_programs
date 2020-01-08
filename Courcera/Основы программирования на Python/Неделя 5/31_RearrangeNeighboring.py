l = list(map(int, input().split()))
for i in range(0, len(l), 2):
    if i + 1 < len(l):
        l[i], l[i + 1] = l[i + 1], l[i]
print(*l)
