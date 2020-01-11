s1, e1, s2, e2 = map(int, input().split())
if s1 < e1:
    set1 = set(range(s1, e1 + 1))
else:
    set1 = set(range(e1, s1 + 1))
if s2 < e2:
    set2 = set(range(s2, e2 + 1))
else:
    set2 = set(range(e2, s2 + 1))
print(len(set1 & set2))
