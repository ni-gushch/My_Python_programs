l = list(map(int, input().split()))
length = len(l)
m = l[0]
j = 0
for i in range(1, length):
    if l[i] > m:
        m = l[i]
        j = i
print(m, j)
