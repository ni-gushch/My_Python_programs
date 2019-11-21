print("Введите число:")
num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
print(((a - d)**2 + (b - c)**2) + 1)
