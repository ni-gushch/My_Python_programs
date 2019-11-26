import math


def MinDivisor(n):
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 5 == 0:
        return 5
    elif n % 7 == 0:
        return 7
    k = 9
    while k <= math.sqrt(n):
        if n % k == 0:
            return k
        k += 1
    return n

n = int(input())
print(MinDivisor(n))
