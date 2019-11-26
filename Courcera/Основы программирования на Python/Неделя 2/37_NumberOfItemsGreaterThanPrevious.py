a = int(input())
k = 0
while a != 0:
    prew = a
    a = int(input())
    if a > prew:
        k += 1
print(k)
