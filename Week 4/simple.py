def IsPrime(n):
    i = 2
    if n == 2:
        return 'YES'
    while n % i != 0:
        i += 1
        if (n % i == 0) and (i <= (n)**0.5):
            return 'NO'
        elif i == (n)**0.5:
            return 'NO'
        elif i > (n)**0.5:
            return "YES"
    return 'NO'


n = int(input())
print(IsPrime(n))
