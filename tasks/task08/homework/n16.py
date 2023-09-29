import itertools as it


alph = 'ВАЙФУ'
res = it.permutations(alph, r=4)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: 'ВФ' not in x and 'ФВ' not in x and x[0] != 'Й', res)
res = len(list(res))
print(res)