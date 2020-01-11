def isPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


print(2, *filter(lambda x: isPrime(x), map(lambda x: x, range(3, int(input()) + 1, 2))))
