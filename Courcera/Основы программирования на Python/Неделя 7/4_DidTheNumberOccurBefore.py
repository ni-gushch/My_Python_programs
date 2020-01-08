l = list(map(int, input().split()))
s = set()
s.add(l[0])
print('NO')
for i in l[1:]:
    if i in s:
        print("YES")
    else:
        print("NO")
        s.add(i)
