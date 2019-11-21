print("Введите трехзначное число:")
number = int(input())
print("Сумма цифр = ", ((number // 100) + ((number % 100) // 10) + number % 10))
