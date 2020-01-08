l = list(map(int, input().split()))
q = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            q += 1
print(q)
