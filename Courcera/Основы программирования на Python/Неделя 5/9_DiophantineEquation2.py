a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = 0
for x in range(0, 1001, 1):
    if x == e:
        continue
    else:
        q = (a * pow(x, 3)) + (b * pow(x, 2)) + (c * x)
        w = -d
        if q == w:
            k += 1
print(k)
