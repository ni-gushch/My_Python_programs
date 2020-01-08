l1 = set(map(int, input().split()))
l2 = set(map(int, input().split()))
l = set.union(l1, l2)
print(len(l1) + len(l2) - len(l))
