l = list(map(int, input().split()))
length = len(l)
for i in range((length - 1), (-1), -1):
    print(l[i], end=' ')
