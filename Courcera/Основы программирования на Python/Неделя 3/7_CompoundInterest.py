p = int(input())
x = int(input())
y = int(input())
k = int(input())
cents = x * 100 + y
while k != 0:
    cents = cents + (cents * (p / 100))
    cents = int(cents)
    k -= 1
print(int(cents // 100), int(cents % 100))
