def Merge(A, B):
    C = []
    j, i = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
        elif A[i] == B[j]:
            C.append(A[i])
            C.append(B[j])
            i += 1
            j += 1
    if i != len(A):
        for k in range(i, len(A)):
            C.append(A[k])
    elif j != len(B):
        for k in range(j, len(B)):
            C.append(B[k])
    return C

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*(Merge(a, b)))
