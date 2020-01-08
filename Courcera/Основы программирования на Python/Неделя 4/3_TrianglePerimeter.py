import math


def perimaretTriangle(x1, y1, x2, y2, x3, y3):
    d1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    d2 = math.sqrt(math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2))
    d3 = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
    p = d1 + d2 + d3
    return p

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
perimeter = perimaretTriangle(x1, y1, x2, y2, x3, y3)
print('{0:.6f}'.format(perimeter))
