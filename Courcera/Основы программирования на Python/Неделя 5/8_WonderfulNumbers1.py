for i in range(10, 100, 1):
    tup = tuple(str(i))
    if 2 * (int(tup[0]) * int(tup[1])) == i:
        print(i)
