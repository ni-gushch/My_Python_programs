i = int(input())
p = 0
k = i
while k > 1:
    if i % k == 0:
        p = k
    k -= 1
print(p)
