def Min4Numbers(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    minRes = min(min1, min2)
    return minRes

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(Min4Numbers(a, b, c, d))
