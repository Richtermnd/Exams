from itertools import permutations


def shift_to_g(s: str):
    """ Зелёных меньше всего, поэтому легче всего по ним выравнивать """
    res = set()
    g = s.find('g')
    res.add(s[g:] + s[:g])

    g = s.find('g', g + 1)
    res.add(s[g:] + s[:g])
    return res


res = []
for perm in set(permutations('bbbbrrrgg')):
    for i in range(len(perm)):
        if perm[i - 1] == perm[i]:
            break
    else:
        res.append(''.join(perm))

temp = []
for elem in res:
    shifted = shift_to_g(elem)
    if shifted not in temp:
        temp.append(shifted)

print(len(temp))



