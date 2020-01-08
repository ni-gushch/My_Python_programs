N, K = map(int, input().split())
bowl = list(range(1, N + 1))
while K != 0:
    Li, Ri = map(int, input().split())
    while Li != Ri + 1:
        bowl[Li - 1] = 0
        Li += 1
    K -= 1
for j in range(len(bowl)):
    if bowl[j] == 0:
        print('.', end='')
    else:
        print('I', end='')
