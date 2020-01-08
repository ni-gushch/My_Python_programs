l = list(map(int, input().split()))
length = len(l)
l.sort()
for i in range(0, length):
    if l[i] > 0:
        print(l[i])
        break
