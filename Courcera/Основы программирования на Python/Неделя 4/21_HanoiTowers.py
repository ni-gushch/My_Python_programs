def hanoi(n, s1, sw, sk):
    def step():
        print(n, s1, sk)
    if n == 1:
        step()
    else:
        hanoi(n - 1, s1, sk, sw)
        step()
        hanoi(n - 1, sw, s1, sk)

n = int(input())
s1 = 1
sw = 2
sk = 3
hanoi(n, s1, sw, sk)
