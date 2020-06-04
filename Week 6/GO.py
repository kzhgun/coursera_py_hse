a = int(input())
b = list(enumerate(map(int, input().split()[:a]), 1))
c = int(input())
d = list(enumerate(map(int, input().split()[:c]), 1))

b.sort(key=lambda k: k[1])
d.sort(key=lambda k: k[1])

index = 0
result = []

for b in b:
    while index + 1 < c and abs((b[1]) - (d[index][1])) > abs(b[1] - d[index + 1][1]):
        index += 1
    else:
        result.append([b[0], d[index][0]])

result.sort(key=lambda k: k[0])

for i in result:
    print(i[1], end=' ')
