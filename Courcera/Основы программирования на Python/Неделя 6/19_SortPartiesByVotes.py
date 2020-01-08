from operator import attrgetter


class Partie:
    Name = ''
    Vote = 0

inFile = open("input.txt", 'r', encoding='utf-8')
lines = inFile.read().splitlines()
partI = lines.index("PARTIES:")
voteI = lines.index("VOTES:")
partiesList = lines[partI + 1:voteI]
votesList = lines[voteI + 1:]
rateL = [0] * len(partiesList)
objectsList = list()
for part in partiesList:
    tempPart = Partie()
    tempPart.Name = part
    tempPart.Vote = votesList.count(part)
    objectsList.append(tempPart)
objectsList.sort(key=lambda x: (-x.Vote, x.Name))
for part in objectsList:
    print(part.Name)
inFile.close()
