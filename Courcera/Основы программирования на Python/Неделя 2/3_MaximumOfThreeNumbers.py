print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
print("Введите третье число")
c = int(input())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > b and c > a:
    print(c)
else:
    if a == b and a > c:
        print(a)
    elif a == b and a < c:
        print(c)
    elif a == c and a > b:
        print(a)
    elif a == c and a < b:
        print(b)
    elif b == c and b > a:
        print(b)
    elif b == c and b < a:
        print(a)
    elif a == b == c:
        print(a)
