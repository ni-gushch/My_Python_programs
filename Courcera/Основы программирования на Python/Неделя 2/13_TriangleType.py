a = int(input())
b = int(input())
c = int(input())
if ((a + b > c) and (a + c > b) and (b + c > a) and
        a > 0 and b > 0 and c > 0):
    if (a > b and a > c) or (a == b and a > c) or (a == b == c):
        biggest = a
        small_1 = b
        small_2 = c
    elif (b > a and b > c) or (a == b and b > c):
        biggest = b
        small_1 = a
        small_2 = c
    elif (c > a and c > b) or (c == b and c > a) or (c == a and c > b):
        biggest = c
        small_1 = b
        small_2 = a
    if biggest**2 == small_1**2 + small_2**2:
        print("rectangular")
    elif biggest**2 > small_1**2 + small_2**2:
        print("obtuse")
    elif biggest**2 < small_1**2 + small_2**2:
        print("acute")
else:
    print("impossible")
