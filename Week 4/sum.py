def sum(a, b):
    while b != 0:
        a += 1
        b -= 1
    return a

a = int(input())
b = int(input())
print(sum(a, b))
