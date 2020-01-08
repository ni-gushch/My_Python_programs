def Intersection(A, B):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
        elif A[i] == B[j]:
            c.append(A[i])
            i += 1
            j += 1
    return(c)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = Intersection(a, b)
print(*c)
