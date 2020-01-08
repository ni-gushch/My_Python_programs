l = list(map(int, input().split()))
k = int(input())
length = len(l)
for i in range(k, length - 1):
    l[i], l[i + 1] = l[i + 1], l[i]
l.pop()
print(*l)
