input()
k = input().split()
def new_variant(a_l:list)->list:
    result = {k:None for k in (a_l)}
    return list((list(result.keys())))
p = new_variant(k)
print(len(p))
p = ' '.join(p)
print(p)