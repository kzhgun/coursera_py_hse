a = open('input.txt', encoding='utf8')
wordsDict = {}
b = a.read().split()
for word in b:
    wordsDict[word] = wordsDict.get(word, -1) + 1
    print(wordsDict[word], end=' ')
