x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def IsPointInCircle(x, y, xc, yc, r):
    return ((((x-xc)**2)+((y-yc)**2))**0.5) > r


if IsPointInCircle(x, y, xc, yc, r):
    print('NO')
else:
    print('YES')
