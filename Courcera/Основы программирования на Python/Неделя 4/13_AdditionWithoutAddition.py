def sum(a, b):
    if b > 0:
        a += 1
        a = sum(a, b - 1)
    return a


a = int(input())
b = int(input())
print(sum(a, b))
