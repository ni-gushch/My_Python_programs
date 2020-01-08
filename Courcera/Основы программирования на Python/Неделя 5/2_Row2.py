a = int(input())
b = int(input())
c = 1
if a > b:
    c = -1
for i in range(a, b + c, c):
    print(i, end=' ')
