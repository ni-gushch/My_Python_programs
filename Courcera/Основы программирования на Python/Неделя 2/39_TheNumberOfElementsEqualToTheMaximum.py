a = int(input())
max = a
k = 1
while a != 0:
    a = int(input())
    if a == max:
        k += 1
    elif a > max:
        max = a
        k = 1
print(k)
