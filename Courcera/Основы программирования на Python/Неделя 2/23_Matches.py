l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
a = [l1, l2, l3]
b = [r1, r2, r3]
a.sort()
b.sort()
if a[1] <= b[0] and a[2] <= b[1]:
    print(0)
else:
    tmp = [[l2, r2], [l3, r3]]
    tmp.sort()
    if r1 - l1 + tmp[0][1] >= tmp[1][0]:
        print(1)
        exit(0)
    tmp = [[l1, r1], [l3, r3]]
    tmp.sort()
    if r2 - l2 + tmp[0][1] >= tmp[1][0]:
        print(2)
        exit(0)
    tmp = [[l1, r1], [l2, r2]]
    tmp.sort()
    if r3 - l3 + tmp[0][1] >= tmp[1][0]:
        print(3)
        exit(0)
    print(-1)
    exit(0)
