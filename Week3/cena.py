

n = int(input())
a = []

for _ in range(n):
    a.append(float(input()))
print(a)
b = int(input())

g = []
for _ in range(2*b):
    for _ in range(2):
        g.append(int(input()))
        print(g)
    h = a[g[0]:g[1+1]]
    print(h)


