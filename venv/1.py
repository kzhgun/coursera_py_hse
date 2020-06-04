s = input()
if ', and' in s or ', or' in s:
    print (s)
else:
    if ',' in s:
        a = s.rfind (' and')
        b = s.rfind (' or')
        if a != -1:
            s = s[:a] + ',' + s[a:]
        elif b != -1:
            s = s[:b] + ',' + s[b:]
    print (s)