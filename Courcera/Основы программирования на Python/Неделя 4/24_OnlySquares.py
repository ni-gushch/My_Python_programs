import math


def SecRevers(k):
    n = int(input())
    if n == 0:
        if(math.sqrt(n) == int(math.sqrt(n)) and n != 0):
            print(n, end=' ')
    else:
        k = SecRevers(k)
        if(math.sqrt(n) == int(math.sqrt(n))):
            print(n, end=' ')
            k += 1
    return k

k = 0
k = SecRevers(k)
if k == 0:
    print(k)
