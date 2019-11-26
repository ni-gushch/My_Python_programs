def ReduceFraction(n, m):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    nod = gcd(n, m)
    return(int(n / nod), int(m / nod))


m = int(input())
n = int(input())
print(*ReduceFraction(m, n))
