inText = open("input.txt")
wordCount = {}
numList = list()
for line in inText:
    wordsInLine = line.split()
    for word in wordsInLine:
        if word not in wordCount:
            k = 0
            wordCount[word] = k
            numList.append(wordCount[word])
        else:
            wordCount[word] += 1
            numList.append(wordCount[word])
print(*numList)
inText.close()
