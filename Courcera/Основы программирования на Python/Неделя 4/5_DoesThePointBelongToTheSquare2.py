import math


def IsPointInSquare(x, y):
    x0, y0 = 0, 0
    x1, y1 = -1, 0
    x2, y2 = 0, 1
    x3, y3 = 1, 0
    x4, y4 = 0, -1
    l1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    Ssqare = math.pow(l1, 2)
    if x == x0 and y == y0:
        return "YES"
    elif x >= 0 and y >= 0:
        Striangle1 = (abs((x0 - x) * (y2 - y) - (x2 - x) * (y0 - y))) / 2
        Striangle2 = (abs((x0 - x) * (y3 - y) - (x3 - x) * (y0 - y))) / 2
    elif x >= 0 and y <= 0:
        Striangle1 = (abs((x0 - x) * (y3 - y) - (x3 - x) * (y0 - y))) / 2
        Striangle2 = (abs((x0 - x) * (y4 - y) - (x4 - x) * (y0 - y))) / 2
    elif x <= 0 and y <= 0:
        Striangle1 = (abs((x0 - x) * (y4 - y) - (x4 - x) * (y0 - y))) / 2
        Striangle2 = (abs((x0 - x) * (y1 - y) - (x1 - x) * (y0 - y))) / 2
    elif x <= 0 and y >= 0:
        Striangle1 = (abs((x0 - x) * (y1 - y) - (x1 - x) * (y0 - y))) / 2
        Striangle2 = (abs((x0 - x) * (y2 - y) - (x2 - x) * (y0 - y))) / 2
    if format(Striangle1 + Striangle2, '.4f') <= format(Ssqare / 4, '.4f'):
        return "YES"
    else:
        return "NO"


x = float(input())
y = float(input())
print(IsPointInSquare(x, y))
