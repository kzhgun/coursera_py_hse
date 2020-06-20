n = int(input())
a = []
for i in range(n):
    c = input().split()
    a.append(c)
a.sort(key=lambda score: int(score[1]), reverse=True)
for i in a:
    print(i[0])
