a = int(input())
while a // 10 != 0:
    print(a % 10, end="", sep="")
    a = a // 10
print(a, end="", sep="")
