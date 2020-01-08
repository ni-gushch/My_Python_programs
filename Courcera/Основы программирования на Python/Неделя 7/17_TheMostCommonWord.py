import sys

inText = sys.stdin.read()
d = {}
m = 0
w = list()
for word in inText.split():
    if word not in d:
        d[word] = 0
    else:
        d[word] += 1
    if d[word] > m:
        w.clear()
        w.append(word)
        m = d[word]
    elif d[word] == m:
        w.append(word)
w.sort()
print(w[0])
