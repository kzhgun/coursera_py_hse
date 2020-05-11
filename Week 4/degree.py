def power(a, n):
    s = 1
    while n != 0:
        s *= a
        n -= 1
    return s

a = float(input())
b = float(input())

print(power(a, b))
