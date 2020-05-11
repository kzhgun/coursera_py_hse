def ReduceFraction(n, m):
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return gcd(m, n % m)
    return n // gcd(n, m), m // gcd(n, m)


n = int(input())
m = int(input())
print(ReduceFraction(n, m))