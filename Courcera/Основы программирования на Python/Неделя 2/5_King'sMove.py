print("Введите номер столбца первой клетки:")
col1 = int(input())
print("Введите номер строки первой клетки:")
row1 = int(input())
print("Введите номер столбца второй клетки:")
col2 = int(input())
print("Введите номер строки второй клетки:")
row2 = int(input())
if (col1 + 0 == col2 and row1 + 0 == row2) or \
        (col1 + 1 == col2 and row1 + 0 == row2) or \
        (col1 + 1 == col2 and row1 + 1 == row2) or \
        (col1 + 0 == col2 and row1 + 1 == row2) or \
        (col1 + -1 == col2 and row1 + 1 == row2) or \
        (col1 + -1 == col2 and row1 + 0 == row2) or \
        (col1 + -1 == col2 and row1 + -1 == row2) or \
        (col1 + 0 == col2 and row1 + -1 == row2) or \
        (col1 + 1 == col2 and row1 + -1 == row2):
    print('YES')
else:
    print('NO')
