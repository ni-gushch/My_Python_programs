class Pupil:
    lastName = ''
    score = 0


def sortByScore(c):
    return (c.score)


n = int(input())
l = []
for i in range(n):
    temp = input().split()
    q = Pupil()
    q.lastName = temp[0]
    q.score = int(temp[1])
    l.append(q)
l.sort(key=sortByScore, reverse=True)
for item in l:
    print(item.lastName)
