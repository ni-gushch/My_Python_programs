def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x - 1)

n = int(input())
s = 0
for i in range(1, n + 1):
    s += fact(i)
print(s)
