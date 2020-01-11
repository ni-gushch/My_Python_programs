inFile = open('input.txt', 'r', encoding='utf-8')
lines = inFile.read().splitlines()
d = dict()
sumV = 0
for line in lines:
    lineS = line.split()
    votes = int(lineS.pop())
    sumV += votes
    name = ''
    for i in lineS:
        name += i + ' '
    name = name.rstrip()
    d[name] = votes
pich = sumV / 450
s = 0
for part in d:
    d[part] = d[part] / pich
    s += int(d[part])
if s < 450:
    k = 450 - s
    l = list()
    for i in d:
        l.append((i, d[i] - int(d[i])))
    l.sort(key=lambda x: x[1], reverse=True)
    for i in range(k):
        d[l[i % len(l)][0]] += 1
for part in d:
    print(part, int(d[part]))
inFile.close()
