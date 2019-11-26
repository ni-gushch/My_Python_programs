import math
a = float(input())
drob = float('{0:.6f}'.format(a % 1))
if drob > 0.5:
    s = math.ceil(a)
elif drob < 0.5:
    s = math.floor(a)
elif drob == 0.5:
    s = math.ceil(a)
print(s)