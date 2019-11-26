import math


a = int(input())
sumPow = 0
sum = 0
k = 0
while a != 0:
    sumPow += pow(a, 2)
    sum += a
    k += 1
    a = int(input())
sigma = (sum / k)
b = (sumPow - (2 * sigma * sum) + (k * math.pow(sigma, 2))) / (k-1)
sko = math.sqrt(b)
print(sko)
