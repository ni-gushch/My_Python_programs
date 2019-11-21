print("Введите X координату 1ой клетки:")
x1 = int(input())
print("Введите Y координату 1ой клетки:")
y1 = int(input())
print("Введите X координату 2ой клетки:")
x2 = int(input())
print("Введите Y координату 2ой клетки:")
y2 = int(input())
if ((x1 == (x2 - 1)) and (y1 == (y2 - 1))) or \
        ((x1 == (x2 - 1)) and (y1 == (y2 + 1))) or \
        ((x1 == (x2 + 1)) and (y1 == (y2 + 1))) or \
        ((x1 == (x2 + 1)) and (y1 == (y2 - 1))):
    print('YES')
else:
    print('NO')
