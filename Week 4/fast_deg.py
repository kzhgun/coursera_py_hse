def Fpower(a, n):
    if n == 0:
        return 1
    if n > 1:
        if n % 2 == 0:
            return Fpower(a * a, n / 2)
        else:
            return a * Fpower(a, n - 1)
    return a


a = float(input())
b = int(input())
print(Fpower(a, b))
