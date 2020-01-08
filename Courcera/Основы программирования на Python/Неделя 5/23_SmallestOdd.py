l = list(map(int, input().split()))
l.sort()
length = len(l)
for i in range(0, length):
    if l[i] != 0 and l[i] % 2 != 0:
        print(l[i])
        break
