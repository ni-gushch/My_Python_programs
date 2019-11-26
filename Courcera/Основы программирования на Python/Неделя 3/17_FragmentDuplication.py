inS = input()
f_h = inS.find('h')
k = f_h
while k != -1:
    l_h = k
    k = inS.find('h', l_h + 1)
print(inS[:f_h + 1], inS[f_h + 1: l_h] * 2, inS[l_h:], sep='')
