l = list(map(int, input().split()))
k = 0
a = 0
for i in range(len(l)):
    m = l.count(l[i])
    if m > k:
        k = m
        a = l[i]
print(a)
