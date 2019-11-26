def SecRevers():
    n = int(input())
    if n == 0:
        print(n)
    else:
        SecRevers()
        print(n)

SecRevers()
