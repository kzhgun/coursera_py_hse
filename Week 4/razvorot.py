def raz():
    n = int(input())
    a = 0
    if n != 0:
        a += n
        raz()
    print(a)


raz()
