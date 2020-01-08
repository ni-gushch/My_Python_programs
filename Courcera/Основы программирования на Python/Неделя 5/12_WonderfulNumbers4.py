a = int(input())
b = int(input())
if a > b:
    a, b = b, a
for i in range(a, b + 1):
    t = tuple(str(i))
    if int(t[0]) == int(t[3]) and int(t[1]) == int(t[2]):
        print(i)
