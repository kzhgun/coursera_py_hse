b = open('input.txt', encoding='utf8')
cDict = {}
i = 0
for line in b:
    cand = line.strip()
    cDict[cand] = cDict.get(cand, 0) + 1
    i += 1
first = max(cDict, key=cDict.get)
out = open('output.txt', 'w', encoding='utf8')
if 2 * cDict[first] > i:
    print(first, file=out)
else:
    print(first, file=out)
    print(sorted(cDict, key=cDict.get, reverse=True)[1],
          file=out)
