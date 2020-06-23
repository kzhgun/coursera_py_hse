myList = list(map(int, input().split()))
mySet = set()
for elem in myList:
    if elem in mySet:
        print('YES')
    else:
        print('NO')
        mySet.add(elem)
