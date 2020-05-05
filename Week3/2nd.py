a = str(input())

b = a.find('f')
c = a[:b] + a[b + 1:]
d = c.find('f')
if b == -1:
    print(f'-2')
elif d == -1:
    print(f'-1')
else:
    print(f'{d+1}')
