n = int(input())
d = dict()
s = set()
l = list()
for i in range(n-1):
    inLine = input().split()
    s.add(inLine[0])
    s.add(inLine[1])
    d[inLine[0]] = inLine[1]
for item in s:
    k = 0
    m = item
    while(m in d):
        k += 1
        m = d[m]
    l.append((item, k))
l.sort(key=lambda x: x[0])
for item in l:
    print(item[0], item[1])
