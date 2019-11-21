k = int(input())
m = int(input())
n = int(input())
if n <= k:
    print(2 * m)
else:
    a = 2 * n
    b = a // k
    if a % k != 0:
        b += 1
    print(b * m)
