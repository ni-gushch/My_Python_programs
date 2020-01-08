a = list(map(int, input().split()))
l = len(a)
k = 0
for i in range(l - 1):
    if a[i] < a[i + 1]:
        print(a[i + 1], end=' ')
