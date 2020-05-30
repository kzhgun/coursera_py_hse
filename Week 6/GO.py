a = int(input())
b = list(enumerate(map(int, input().split()[:a]), 1))
c = int(input())
d = list(enumerate(map(int, input().split()[:c]), 1))

b.sort(key=lambda k: k[1])
d.sort(key=lambda k: k[1])

print(b)
