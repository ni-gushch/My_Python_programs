l = list(map(int, input().split()))
k = l[0]
q = 0
for i in range(0, len(l)):
    if l.count(l[i]) == 1:
        print(l[i], end=' ')
