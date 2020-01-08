import math


def Lagrange(n, i2, j2, k2, m2):
    i = 0
    while i2 < n:
        i2 = j2 = i*i
        j = i
        while (i2 + j2) < n:
            j2 = k2 = j*j
            k = j
            while (i2 + j2 + k2) < n:
                k2 = m2 = k*k
                m = k
                while (i2 + j2 + k2 + m2) <= n:
                    m2 = m * m
                    if (i2 + j2 + k2 + m2 == n):
                        if i2 != 0:
                            print(int(math.sqrt(i2)), end=' ')
                        if j2 != 0:
                            print(int(math.sqrt(j2)), end=' ')
                        if k2 != 0:
                            print(int(math.sqrt(k2)), end=' ')
                        if m2 != 0:
                            print(int(math.sqrt(m2)), end=' ')
                        return
                    m += 1
                k += 1
            j += 1
        i += 1

n = int(input())
Lagrange(n, 0, 0, 0, 0)
