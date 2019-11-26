l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
h = max(h1, h2)
if l1 + l2 <= lc and max(w1, w2) <= wc and h <= hc:
    print("YES")
elif l1 + w2 <= lc and max(w1, l2) <= wc and h <= hc:
    print("YES")
elif w1 + l2 <= lc and max(l1, w2) <= wc and h <= hc:
    print("YES")
elif w1 + w2 <= lc and max(l1, l2) <= wc and h <= hc:
    print("YES")
elif l1 + l2 <= wc and max(w1, w2) <= lc and h <= hc:
    print("YES")
elif l1 + w2 <= wc and max(w1, l2) <= lc and h <= hc:
    print("YES")
elif w1 + l2 <= wc and max(l1, w2) <= lc and h <= hc:
    print("YES")
elif w1 + w2 <= wc and max(l1, l2) <= lc and h <= hc:
    print("YES")
elif h1 + h2 <= hc and max(l1, l2) <= lc and max(w1, w2) <= wc:
    print("YES")
elif h1 + h2 <= hc and max(l1, w2) <= lc and max(w1, l2) <= wc:
    print("YES")
elif h1 + h2 <= hc and max(l1, l2) <= wc and max(w1, w2) <= lc:
    print("YES")
elif h1 + h2 <= hc and max(l1, w2) <= wc and max(w1, l2) <= lc:
    print("YES")
else:
    print("NO")
