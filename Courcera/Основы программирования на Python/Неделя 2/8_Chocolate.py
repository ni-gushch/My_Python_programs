print("Длина шоколадки:")
n = int(input())
print("Ширина шоколадки:")
m = int(input())
print("Количество долек:")
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
