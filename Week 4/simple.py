def IsPrime(n):
    i = 2
    while i < (n)**0.5 and n % i != 0:
        i += 1
        return 'YES'
    return 'NO'


n = int(input())
print(IsPrime(n))
