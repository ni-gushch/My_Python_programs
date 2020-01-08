inFile = open('input.txt', 'r', encoding='utf-8')
k9 = 0
k10 = 0
k11 = 0
for item in inFile.readlines():
    temp = item.split()
    if int(temp[2]) == 9:
        if int(temp[3]) > k9:
            k9 = int(temp[3])
    elif int(temp[2]) == 10:
        if int(temp[3]) > k10:
            k10 = int(temp[3])
    elif int(temp[2]) == 11:
        if int(temp[3]) > k11:
            k11 = int(temp[3])
print(k9, k10, k11)
inFile.close()
