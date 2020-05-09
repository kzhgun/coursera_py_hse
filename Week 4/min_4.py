a1 = int(input())
b2 = int(input())
c3 = int(input())
d4 = int(input())


def min4(a, b, c, d):
    s = min(a, b)
    p = min(c, d)
    q = min(s, p)
    print(q)


min4(a1, b2, c3, d4)
