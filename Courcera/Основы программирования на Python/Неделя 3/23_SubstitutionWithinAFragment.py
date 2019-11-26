inS = input()
f_h = inS.find('h')
k = f_h
while k != -1:
    l_h = k
    k = inS.find('h', l_h + 1)
modS = inS[f_h + 1:l_h]
print(inS[:f_h + 1], modS.replace('h', 'H'), inS[l_h:], sep='')
