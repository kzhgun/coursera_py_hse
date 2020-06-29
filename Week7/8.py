n = int(input())
b = dict(input().split() for i in range(n))
k = str(input())
for keys, items in b.items():
    if k in keys:
        print(items)
    elif k in items:
        print(keys)
