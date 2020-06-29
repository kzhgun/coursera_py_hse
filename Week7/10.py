b = open('input.txt', encoding='utf8')
b = b.read().split()
c = {}
for a in b:
    if a not in c:
        c[a] = 1
    else:
        c[a] += 1
print(*sorted(sorted(c), key=lambda x: c[x], reverse=True),
      sep="\n")
