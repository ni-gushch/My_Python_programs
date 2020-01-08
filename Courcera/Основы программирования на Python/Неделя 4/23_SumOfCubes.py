import math


def Lagrange(n, i2, j2, k2, m2, l2, o2, p2):
    i = 0
    while i2 < n:
        i2 = j2 = i*i*i
        j = i
        while (i2 + j2) < n:
            j2 = k2 = j*j*j
            k = j
            while (i2 + j2 + k2) < n:
                k2 = m2 = k*k*k
                m = k
                while (i2 + j2 + k2 + m2) < n:
                    m2 = l2 = m * m * m
                    l = m
                    while (i2 + j2 + k2 + m2 + l2) < n:
                        l2 = o2 = l * l * l
                        o = l
                        while (i2 + j2 + k2 + m2 + l2 + o2) < n:
                            o2 = p2 = o * o * o
                            p = o
                            while (i2 + j2 + k2 + m2 + l2 + o2 + p2) <= n:
                                p2 = p * p * p
                                if (i2 + j2 + k2 + m2 + l2 + o2 + p2 == n):
                                    if i2 != 0:
                                        print(int(i2), end=' ')
                                    if j2 != 0:
                                        print(int(j2), end=' ')
                                    if k2 != 0:
                                        print(int(k2), end=' ')
                                    if m2 != 0:
                                        print(int(m2), end=' ')
                                    if l2 != 0:
                                        print(int(l2), end=' ')
                                    if o2 != 0:
                                        print(int(o2), end=' ')
                                    if p2 != 0:
                                        print(int(p2), end=' ')
                                    return
                                p += 1
                            o += 1
                        l += 1
                    m += 1
                k += 1
            j += 1
        i += 1
    print(0)

n = int(input())
Lagrange(n, 0, 0, 0, 0, 0, 0, 0)
