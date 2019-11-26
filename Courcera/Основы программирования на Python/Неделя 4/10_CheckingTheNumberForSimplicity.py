import math


def IsPrime(n):
    k = 2
    while k <= math.sqrt(n):
        if n % k == 0:
            return False
        k += 1
    return True

num = int(input())
if IsPrime(num):
    print("YES")
else:
    print("NO")
