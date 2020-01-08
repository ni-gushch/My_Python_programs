l = list(map(int, input().split()))
length = len(l)
k = 0
for i in range(1, length - 1):
    if l[i - 1] < l[i] > l[i + 1]:
        k += 1
print(k)
