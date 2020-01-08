N = int(input())
l = list(map(int, input().split()))
x = int(input())
m = 2001
k = 0
for i in range(N):
    if abs(x - l[i]) < m:
        m = abs(x - l[i])
        k = l[i]
print(k)
