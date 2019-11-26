a = int(input())
fn_2 = 0
fn_1 = 1
fn = 0
n = 1
while fn < a:
    fn = fn_2 + fn_1
    fn_2 = fn_1
    fn_1 = fn
    n += 1
if a == 0:
    print(0)
elif a == 1:
    print(1)
elif fn == a:
    print(n)
elif fn != a:
    print(-1)
