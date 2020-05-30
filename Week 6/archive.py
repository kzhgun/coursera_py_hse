a = list(map(int, input().split()))
s = []
summ = 0
n = 0
p = 0
for i in range(0, a[1]):
    k = int(input())
    s.append(k)
s.sort()

for j in range(len(s)):
    summ = summ + s[j]
    if a[0] > summ:
        p += 1
print(p)
