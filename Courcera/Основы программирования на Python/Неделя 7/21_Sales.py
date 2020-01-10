inFile = open('input.txt', 'r', encoding='utf-8')
d = dict()
for line in inFile:
    temp = line.strip().split()
    user = temp[0]
    prod = temp[1]
    count = int(temp[2])
    if user in d:
        d[user][prod] = d[user].get(prod, 0) + count
    else:
        d[user] = {}
        d[user][prod] = count
for u in sorted(d):
    print(u, ':', sep='')
    for p in sorted(d[u]):
        print(p, d[u][p])
inFile.close()
