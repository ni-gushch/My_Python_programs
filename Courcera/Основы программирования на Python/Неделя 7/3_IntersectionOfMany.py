s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
for i in sorted(s1 & s2):
    print(i, end=' ')
