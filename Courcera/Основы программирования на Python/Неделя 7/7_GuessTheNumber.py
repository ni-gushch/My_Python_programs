n = int(input())
ans = ''
resSet = set(range(1, n + 1))
while ans != "HELP":
    st = str(input())
    if st != "HELP":
        s = set(map(int, st.split()))
        ans = str(input())
        if ans == "YES":
            resSet &= s
        elif ans == "NO":
            resSet -= s
    else:
        ans = st
for i in sorted(resSet):
    print(i, end=' ')
