l = list(map(int, input().split()))
q = l[0]
k = [q, ]
j = 0
for i in range(1, len(l)):
    if l[i] != k[j]:
        k.append(l[i])
        j += 1
print(len(k))
