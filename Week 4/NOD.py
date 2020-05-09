
def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i < (n)**0.5:
            i += 1
        else:
            return n
    return i


n = int(input())
print(MinDivisor(n))
