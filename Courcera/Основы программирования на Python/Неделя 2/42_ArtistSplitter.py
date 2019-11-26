a = int(input())
b = int(input())
while a != b:
    if a == 2:
        a = a / 2
        print(":2")
    elif a % 2 == 0:
        c = a / 2
        if c < b:
            a = a - 1
            print("-1")
        else:
            a = c
            print(":2")
    elif a % 2 != 0:
        a = a - 1
        print("-1")
