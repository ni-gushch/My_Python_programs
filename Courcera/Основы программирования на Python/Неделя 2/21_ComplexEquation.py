a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a == 0 and b != 0):
    print("NO")
elif (a == 0 and b == 0):
    print("INF")
elif (b * c == a * d):
    print("NO")
else:
    if -b % a == 0:
        x = -b / a
        print(int(x))
    else:
        print("NO")
