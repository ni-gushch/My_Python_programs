import math


a, b, c = float(input()), float(input()), float(input())
if a == 0 and b == 0 and c == 0:
    print(3)
elif a == 0 and b != 0:
    x = -c / b
    print(1, '{0:.6f}'.format(x))
elif a == 0 and b == 0:
    print(0)
else:
    D = math.pow(b, 2) - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        if '{0:.6f}'.format(x1 % 1) == 0:
            x1 = int(x1)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        if '{0:.6f}'.format(x2 % 1) == 0:
            x1 = int(x2)
        if x1 > x2:
            print(2, '{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
        else:
            print(2, '{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
    elif D == 0:
        x1 = -b / (2 * a)
        if '{0:.6f}'.format(x1 % 1) == 0:
            x1 = int(x1)
        print(1, '{0:.6f}'.format(x1))
    else:
        print(0)
