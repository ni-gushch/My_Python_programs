l = list(map(int, input().split()))
maximum = l[0]
iMaximum = 0
minimum = l[0]
iMinimum = 0
for i in range(len(l)):
    if l[i] >= maximum:
        maximum = l[i]
        iMaximum = i
    if l[i] <= minimum:
        minimum = l[i]
        iMinimum = i
l[iMaximum], l[iMinimum] = l[iMinimum], l[iMaximum]
print(*l)
