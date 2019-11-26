a = int(input())
n = 1
m = n
b = ""
k = 0
if a == 1:
    k += 1
while n != a:
    while m // 10 != 0:
        b += str(m % 10)
        m = m // 10
    b += str(m % 10)
    m = int(b)
    if m == n:
        k += 1
    n += 1
    m = n
    b = ""
print(k)
