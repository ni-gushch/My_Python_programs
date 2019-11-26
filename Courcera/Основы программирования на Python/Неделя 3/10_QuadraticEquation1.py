import math

a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    if '{0:.6f}'.format(x1 % 1) == 0:
        x1 = int(x1)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    if '{0:.6f}'.format(x2 % 1) == 0:
        x1 = int(x2)
    if x1 > x2:
        print('{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
    else:
        print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
elif D == 0:
    x1 = -b / (2 * a)
    if '{0:.6f}'.format(x1 % 1) == 0:
        x1 = int(x1)
    print('{0:.6f}'.format(x1))
else:
    print()
