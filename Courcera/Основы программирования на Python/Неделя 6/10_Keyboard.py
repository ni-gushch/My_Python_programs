n = int(input())
C = list(map(int, input().split()))
k = int(input())
P = list(map(int, input().split()))
Ci = [0] * n
for p in P:
    Ci[p - 1] += 1
for i in range(n):
    if Ci[i] > C[i]:
        print("YES")
    else:
        print("NO")
