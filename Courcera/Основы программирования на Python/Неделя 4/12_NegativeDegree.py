def power(a, n):
    k = 1
    mnozh = a
    if n == 1:
        return a
    if n == 0:
        return 1
    if n > 1:
        while k != n:
            a *= mnozh
            k += 1
        return a
    if n < 0:
        while k != abs(n):
            a *= mnozh
            k += 1
        return 1 / a


a = float(input())
n = int(input())
print('{0:.6f}'.format(power(a, n)))
