def xor(x, y):
    if x == 1 and y == 0:
        return 1
    elif y == 1 and x == 0:
        return 1
    else:
        return 0

x = int(input())
y = int(input())
print(xor(x, y))
