a = str(input())

b = a.find('f')
c = a.rfind('f')
if b == -1 and c == -1:
    print(f'')
elif b == c:
    print(f'{b}')
else:
    print(f'{b} {c}')
