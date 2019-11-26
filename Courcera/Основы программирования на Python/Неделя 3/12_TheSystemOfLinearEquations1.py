a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if b == 0:
    x = e / a
    y = (f - c * x) / (d)
else:
    x = (b * f - d * e) / (b * c - d * a)
    y = (e - a * (x)) / b
print('{0:.6f}'.format(x), '{0:.6F}'.format(y))
