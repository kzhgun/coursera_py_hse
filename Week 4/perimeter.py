x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())


def distance(a, b, c, d):
    dis = (((c-a)**2)+((d-b)**2))**0.5
    return dis


def perimetr(x1, y1, x2, y2, x3, y3):
    return distance(x1, y1, x2, y2) + distance(x1, y1, x3, y3) \
           + distance(x2, y2, x3, y3)


print(perimetr(x1, y1, x2, y2, x3, y3))
