def TelNumConv(num: str):
    shortNum = ''
    codeNum = ''
    num = num.replace('-', '')
    num = num.replace('(', '')
    num = num.replace(')', '')
    if len(num) == 7:
        codeNum = '495'
        shortNum = num
    elif len(num) > 7 and num[0:2] == '+7':
        codeNum = num[2:5]
        shortNum = num[5:]
    elif len(num) > 7 and num[0] == '8':
        codeNum = num[1:4]
        shortNum = num[4:]
    return(codeNum + shortNum)

d = dict()
num1 = input()
num2 = input()
d[num2] = TelNumConv(num2)
num3 = input()
d[num3] = TelNumConv(num3)
num4 = input()
d[num4] = TelNumConv(num4)
nL = (num2, num3, num4)
for i in nL:
    if d[i] == TelNumConv(num1):
        print("YES")
    else:
        print("NO")
