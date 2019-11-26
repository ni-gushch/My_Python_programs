p = int(input())
x = int(input())
y = int(input())
pennies = x * 100 + y
amountInPenniesBefore = pennies + pennies*p/100
amountInRubles = int(amountInPenniesBefore // 100)
amountInPenniesAfter = int(amountInPenniesBefore % 100)
print(amountInRubles, amountInPenniesAfter)
