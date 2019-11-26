x = int(input())
y = int(input())
k = 1
while x < y:
    x += 0.1 * x
    k += 1
print(k)

