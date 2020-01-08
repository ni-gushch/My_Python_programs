l = list(map(int, input().split()))
r = int(input())
k = len(l) + 1
for i in range(len(l)):
    if l[i] - r < 0:
        k = (i + 1)
        break
print(k)
