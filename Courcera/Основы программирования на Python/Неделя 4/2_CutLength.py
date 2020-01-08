import math


def distance(x1, y1, x2, y2):
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return d

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
d = distance(x1, y1, x2, y2)
print('{0:.6f}'.format(d))
