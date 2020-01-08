a = list(input().split())
m = int(a[0])
i = 0
k = 0
for j in a:
    if int(j) > m:
        m = int(j)
        i = k
    elif int(j) == m:
        i = k
    k += 1
print(m, i)
