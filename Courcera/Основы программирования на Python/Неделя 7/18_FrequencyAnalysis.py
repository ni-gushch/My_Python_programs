import sys

inText = sys.stdin.read()
d = {}
l = list()
for word in inText.split():
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
for i in d:
    l.append((d[i], i))
l.sort(key=lambda word: (-word[0], word[1]))
for j in l:
    print(j[1])
