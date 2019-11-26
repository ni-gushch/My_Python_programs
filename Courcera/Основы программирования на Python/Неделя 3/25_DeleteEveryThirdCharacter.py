inS = input()
k = 0
leng = len(inS)
newS = ''
while k != leng:
    if k % 3 == 0:
        a = inS[k]
        # inS = inS.replace(a, '')
    else:
        newS += inS[k]
    k += 1
print(newS)
