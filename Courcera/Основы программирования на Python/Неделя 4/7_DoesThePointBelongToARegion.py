import math


def IsPointInArea(x, y):
    Rx0, Ry0, Rr = -1, 1, 2
    a1, b1 = 2, 2
    a2, b2 = -1, 0
    cond1_1 = y <= (a1 * x + b1)
    cond1_2 = y <= (a2 * x + b2)
    cond1_3 = (pow(x - Rx0, 2) + pow(y - Ry0, 2)) >= pow(Rr, 2)
    cond2_1 = y >= (a1 * x + b1)
    cond2_2 = y >= (a2 * x + b2)
    cond2_3 = (pow(x - Rx0, 2) + pow(y - Ry0, 2)) <= pow(Rr, 2)
    if cond1_1 and cond1_2 and cond1_3:
        return("YES")
    elif cond2_1 and cond2_2 and cond2_3:
        return("YES")
    else:
        return("NO")

x = float(input())
y = float(input())
print(IsPointInArea(x, y))
