a = open('input.txt', 'r', encoding='utf8')
b = open('output.txt', 'w', encoding='utf8')
c = []
for line in a:
    line = line.split(' ')
    line.pop(2)
    c.append(line)
c.sort()
a.close()
for i in range(len(c)):
    print(*c[i])
