a = int(input())
max1 = a
max2 = 0
while a != 0:
    a = int(input())
    if a > max2 < max1:
        max2 = a
    if a > max1:
        max2 = max1
        max1 = a
print(max2)
