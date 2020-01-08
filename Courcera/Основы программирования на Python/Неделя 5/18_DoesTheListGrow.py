def IsAscending(L):
    i = 1
    l = len(L)
    m = L[0]
    while i <= l - 1 and m < L[i]:
        m = L[i]
        i += 1
    return not bool(l - i)

l = list(map(int, input().split()))
if IsAscending(l):
    print("YES")
else:
    print("NO")
