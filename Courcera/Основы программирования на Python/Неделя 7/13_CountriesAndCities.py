n = int(input())
d = dict()
for i in range(n):
    line = input().split()
    lLine = len(line)
    country = line[0]
    for town in line[1:lLine]:
        d[town] = country
m = int(input())
for i in range(m):
    print(d[input()])
