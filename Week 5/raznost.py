n = int(input())
a = list(map(int, input().split()))
b = int(input())
min = 10000
q = 0
if n < 1:
    print(*a)
else:
    for i in range(0, n):
        if abs(a[i] - b) <= min:
            min = abs(a[i] - b)
            q = a[i]
    print(q)
