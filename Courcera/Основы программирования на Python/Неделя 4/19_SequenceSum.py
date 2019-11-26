def SeqSum():
    n = int(input())
    if n == 0:
        return 0
    else:
        n += SeqSum()
        return n

print(SeqSum())
