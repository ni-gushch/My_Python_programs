inFile = open("input.txt", 'r', encoding='utf-8')
lines = inFile.read().splitlines()
partI = lines.index("PARTIES:")
voteI = lines.index("VOTES:")
partiesList = lines[partI + 1:voteI]
votesList = lines[voteI + 1:]
rateL = [0] * len(partiesList)
i = 0
for part in partiesList:
    if(votesList.count(part) / len(votesList) >= 0.07):
        print(part)
    i += 1
inFile.close()
