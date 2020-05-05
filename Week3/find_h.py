a = str(input())

b = a.find('h')
c = a.rfind('h')
print(f'{a[0:b]}{a[c+1:]}')
