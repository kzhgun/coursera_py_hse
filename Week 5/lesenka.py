n = int(input())

for i in range(1, n+1):
    i += 1
    print(*tuple(range(1, i)), sep='')
