inFile = open('input.txt', 'r', encoding='utf-8')
operations = inFile.read().splitlines()
bL = dict()
for line in operations:
    el = line.split()
    if el[0] == 'DEPOSIT':
        if el[1] not in bL:
            bL[el[1]] = 0
        bL[el[1]] = bL[el[1]] + int(el[2])
    elif el[0] == 'WITHDRAW':
        if el[1] not in bL:
            bL[el[1]] = 0
        bL[el[1]] = bL[el[1]] - int(el[2])
    elif el[0] == 'BALANCE':
        if el[1] not in bL:
            print('ERROR')
        else:
            print(bL[el[1]])
    elif el[0] == 'TRANSFER':
        if el[1] not in bL:
            bL[el[1]] = 0
        if el[2] not in bL:
            bL[el[2]] = 0
        bL[el[1]] = bL[el[1]] - int(el[3])
        bL[el[2]] = bL[el[2]] + int(el[3])
    elif el[0] == 'INCOME':
        for cl in bL:
            if bL[cl] > 0:
                bL[cl] = int(bL[cl] * (1 + int(el[1]) / 100))
inFile.close()
