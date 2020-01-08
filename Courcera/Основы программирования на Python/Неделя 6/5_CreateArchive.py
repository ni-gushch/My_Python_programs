S, N = map(int, input().split())
sFU = []
while N != 0:
    sFU.append(int(input()))
    N -= 1
sFU.sort()
sum = 0
k = 0
for i in sFU:
    sum += i
    if sum > S:
        break
    k += 1
print(k)
