import sys

l = sys.stdin.read()
s = set(map(str, l.split()))
print(len(s))
