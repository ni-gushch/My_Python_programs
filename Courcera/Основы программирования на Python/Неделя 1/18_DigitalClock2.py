print("Введите время в секундах:")
a = int(input())
inDaySec = 24 * 60 * 60
today = a % inDaySec
s = today % 60
h = today // 3600
m = ((today - s) % 3600) // 60
print(h, ':', str(m).zfill(2), ':', str(s).zfill(2), sep='')
