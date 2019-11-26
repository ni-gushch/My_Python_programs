def IsPointInSquare(x, y):
    if (-1 <= x <= 1) and (-1 <= y <= 1):
        return "YES"
    return "NO"

x = float(input())
y = float(input())
print(IsPointInSquare(x, y))
