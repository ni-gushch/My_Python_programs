inFile = open('input.txt', 'r', encoding='utf-8')
outFile = open("output.txt", "w", encoding='utf-8')
lines = inFile.read().splitlines()
allVotes = len(lines)
l = list()
d = {}
for line in lines:
    if line not in d:
        d[line] = 1
    else:
        d[line] += 1
for i in d:
    l.append((d[i], i))
l.sort(key=lambda w: [(-w[0], w[1])])
if l[0][0] > allVotes / 2:
    print(l[0][1], file=outFile)
else:
    print(l[0][1], file=outFile)
    print(l[1][1], file=outFile)
inFile.close()
outFile.close()
