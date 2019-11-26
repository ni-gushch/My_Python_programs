x = int(input())
y = int(input())
z = int(input())
k = 0
n = 0
m = 0
while z != 0:
    k += 1
    if y > z and x < y:
        n += 1
        if (n > 1 and (n == 2 or n > 2 and k < m)):
            m = k
        k = 0
    x = y
    y = z
    z = int(input())
print(m)
