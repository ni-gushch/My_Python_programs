a = int(input())
b = a
k = 1
max = k
while a != 0:
    if a > b:
        if k > max:
            max = k
        k = 1
        while a > b and a > 0:
            k += 1
            b = a
            a = int(input())
    if a < b:
        if k > max:
            max = k
        k = 1
        while a < b and a > 0:
            k += 1
            b = a
            a = int(input())
    if a == b:
        if k > max:
            max = k
        k = 1
        b = a
        a = int(input())
if k > max:
    print(k)
else:
    print(max)
