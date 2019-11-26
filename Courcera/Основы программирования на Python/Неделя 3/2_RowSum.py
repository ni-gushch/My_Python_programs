a = int(input())
s = 0
i = 1
while i <= a:
    s += (1 / (i**2))
    i += 1
print('{0:.10f}'.format(s))