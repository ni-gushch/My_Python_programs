a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print(5)
elif a == 0 and b == 0 and c == 0 and d == 0:
    print(0)
elif (a == 0 and b == 0 and c == 0):
    if f != 0:
        print(4, '{0:.6f}'.format(f / d))
    else:
        print(4, 0)
elif (a == 0 and c == 0 and d == 0):
    if e != 0:
        print(4, '{0:.6f}'.format(e / b))
    else:
        print(4, 0)
elif (b == 0 and c == 0 and d == 0):
    if e != 0:
        print(3, '{0:.6f}'.format(e / a))
    else:
        print(3, 0)
elif (a == 0 and b == 0 and d == 0):
    if f != 0:
        print(3, '{0:.6f}'.format(f / c))
    else:
        print(3, 0)
else:
    determinant = a * d - b * c
    determinantX1 = e * d - b * f
    determinantX2 = a * f - e * c
    if a == 0 and c == 0:
        if e * d == b * f and b != 0:
            print(4, '{0:.6f}'.format(e / b))
        else:
            print(0)
    elif b == 0 and d == 0:
        if e * c == a * f and a != 0:
            print(3, '{0:.6f}'.format(e / a))
        else:
            print(0)
    elif determinant == 0:
        if determinantX1 == 0 and determinantX2 == 0:
            if f != 0:
                if e % f == 0:
                    print(1, '{0:.6f}'.format(-c / d), '{0:.6f}'.format(f / d))
                elif f % e == 0:
                    print(1, '{0:.6f}'.format(-c / d), '{0:.6f}'.format(f / d))
            elif e != 0:
                if f % e == 0:
                    print(1, '{0:.6f}'.format(-a / b), '{0:.6f}'.format(e / b))
                elif e % f == 0:
                    print(1, '{0:.6f}'.format(-a / b), '{0:.6f}'.format(e / b))
            elif max(b, d) % min(b, d) == 0 and max(a, c) % min(a, c) == 0:
                print(1, '{0:.6f}'.format(-a / b), 0)
            else:
                print(5)
        else:
            print(0)
    elif determinant != 0:
        x1 = determinantX1 / determinant
        x2 = determinantX2 / determinant
        print(2, '{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
