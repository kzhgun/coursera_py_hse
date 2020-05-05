a = str(input())

b = a.find('f')
c = a.rfind('f')
if b == c:
    print(f'{b}')
else:
    print(f'{b} {c}')
