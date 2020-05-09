n = int(input())
k = input().split()
for _ in range(n):
    k = [j for i, j in enumerate(k) if j not in k[i+1::]]
    print(k)

k = k[::-1]
k = ' '.join(k)
print(k)

