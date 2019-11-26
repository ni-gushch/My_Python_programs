import math


n = int(input())
x = float(input())
a = float(input())
res = a
while n != 0:
    a = float(input())
    res = res * x + a
    n -= 1
print('{0:.3f}'.format(res))
