num = int(input())
my_Set = set([x for x in range(1, num + 1)])
ans_set = input()
b = set()
while ans_set != 'HELP':
    answer = str(input())
    if answer == 'YES':
        ans_set = set(map(int, ans_set.split()))
        my_Set &= ans_set
    elif answer == 'NO':
        ans_set = set(map(int, ans_set.split()))
        b |= ans_set
    ans_set = input()
print(*sorted(list(my_Set - b)))
