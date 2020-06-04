a = input()

if ',' in a:
    a = list(a.split())
    if len(a) >= 2:
        for i in range (-len (a), 1):
            if a[i] == 'or' and ',' not in a[i - 1] and ';' not in a[i - 1]:
                a[i - 1] = a[i - 1] + ','
                break
            if a[i] == 'and' and ',' not in a[i - 1] and ';' not in a[i - 1]:
                a[i - 1] = a[i - 1] + ','
                break
        print (*a)
else:
    print (a)
