a = list(map(int, input().split()))
min = 1000
for i in range(len(a)):
    if a[i] > 0:
        if a[i] < min:
            min = a[i]

print(min)
