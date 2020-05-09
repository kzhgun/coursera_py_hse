input()
a = list(map(float, input().split()))
n = int(input())
def func(a1):
    summ = 0
    for i in range(n):
        q, p = map(int, input().split())
        for el in a1[q:p + 1]:
            summ += 1 / el
        print("{0:.6f}".format((p - q + 1) / summ))

func(a)
