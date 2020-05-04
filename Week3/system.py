a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a != 0 and (a * d - c * b):
    y = (a * f - c * e) / (a * d - c * b)
    x = (e - b * y) / a
else:
    y = e/b
    x = (f-d*y)/c


print(f'{x} {y}')
