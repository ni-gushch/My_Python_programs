l = list(map(int, input().split()))
max1 = -100000
max2 = -100000
max3 = -100000
min1 = 100000
min2 = 100000
min3 = 100000
for i in range(len(l)):
    x = l[i]
    if x > max3:
        max1, max2, max3 = max2, max3, x
    elif x > max2:
        max1, max2 = max2, x
    elif x > max1:
        max1 = x
    if x < min3:
        min1, min2, min3 = min2, min3, x
    elif x < min2:
        min1, min2 = min2, x
    elif x < min1:
        min1 = x
maxMult_1 = max1 * max2 * max3
maxMult_2 = max3 * min3 * min2
if maxMult_1 >= maxMult_2:
    print(max1, max2, max3)
else:
    print(max3, min2, min3)
