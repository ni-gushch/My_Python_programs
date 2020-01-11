n, k = map(int, input().split())
week = set()
work = set()
for i in range(1, n + 1):
    if (i + 1) % 7 == 0 or i % 7 == 0:
        week.add(i)
    else:
        work.add(i)
m = set()
for i in range(k):
    start, step = map(int, input().split())
    rTemp = set(range(start, n + 1, step))
    m = m | (rTemp - week)
print(len(m))
