print("Введите делимое:")
a = int(input())
print("Введите делитель:")
b = int(input())
c = a % b
d = c == 0
print('YES' * int(d), 'NO' * int(1 - d), sep='')
