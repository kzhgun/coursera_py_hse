b = input()
i=0
for i in len(b):
    if b[i].isalpha():
        i +=1
    elif b[i] == '[':
        a=i
        while b[i] != ']':


print(i)

