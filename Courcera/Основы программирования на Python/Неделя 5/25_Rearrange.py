l = list(map(int, input().split()))
length = len(l)
for i in range(0, length // 2):
    l[i], l[length - 1 - i] = l[length - 1 - i], l[i]
print(*l)
