a = int(input())
k = 1
max = 0
m = a
while a != 0:
    a = int(input())
    if a == m:
        k += 1
    else:
        m = a
        if k > max:
            max = k
        k = 1
print(max)
