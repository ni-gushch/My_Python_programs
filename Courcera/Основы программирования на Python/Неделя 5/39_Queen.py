a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4, b4 = map(int, input().split())
a5, b5 = map(int, input().split())
a6, b6 = map(int, input().split())
a7, b7 = map(int, input().split())
a8, b8 = map(int, input().split())
f = []
f.append([a1, b1])
f.append([a2, b2])
f.append([a3, b3])
f.append([a4, b4])
f.append([a5, b5])
f.append([a6, b6])
f.append([a7, b7])
f.append([a8, b8])
k = 1
for i in f:
    for j in f[k:]:
        if abs(i[0] - j[0]) == abs(i[1] - j[1]):
            print('YES')
            exit(0)
        elif i[0] == j[0] or i[1] == j[1]:
            print('YES')
            exit(0)
    k += 1
print('NO')
exit(0)
