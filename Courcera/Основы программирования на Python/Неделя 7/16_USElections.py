inFile = open('input.txt', 'r', encoding='utf-8')
lines = inFile.read().splitlines()
d = dict()
for line in lines:
    temp = line.split()
    if temp[0] not in d:
        d[temp[0]] = int(temp[1])
    else:
        d[temp[0]] += int(temp[1])
for i in sorted(d):
    print(i, d[i])
inFile.close()
