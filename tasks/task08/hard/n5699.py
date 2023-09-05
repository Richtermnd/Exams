from itertools import permutations


ticket = '12345'

perms = permutations('01234567', r=5)

res = 0
for perm in perms:
    mat = 0
    contain = 0
    for a, b in zip(ticket, perm):
        if a == b:
            mat += 1
        elif a in perm:
            contain += 1
    if mat == 2 and contain >= 2:
        res += 1
        # print(''.join(perm), ticket)
        # print(res)
print(res)
