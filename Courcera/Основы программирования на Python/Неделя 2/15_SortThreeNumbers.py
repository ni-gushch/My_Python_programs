a = int(input())
b = int(input())
c = int(input())

if (a == b and a > c) or (b == c and a > b) or (a == b == c):
    x = a
    y = b
    z = c
elif a == b and c > a:
    x = c
    y = a
    z = b
elif a == c and a > b:
    x = a
    y = c
    z = b
elif a == c and b > a:
    x = b
    y = a
    z = c
elif b == c and b > a:
    x = b
    y = c
    z = a
elif a > b and a > c:
    x = a
    if b > c:
        y = b
        z = c
    elif c > b:
        y = c
        z = b
elif b > a and b > c:
    x = b
    if a > c:
        y = a
        z = c
    elif c > a:
        y = c
        z = a
elif c > b and c > a:
    x = c
    if b > a:
        y = b
        z = a
    elif a > b:
        y = a
        z = b

print(z, y, x)
