x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    return -1 <= (abs(x)+abs(y)) <= 1


if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
