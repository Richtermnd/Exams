import itertools as it


alph = 'ВИШНЯ'
res = it.product(alph, repeat=6)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x.count('В') <= 1 and x[0] != 'Ш' and x[-1] not in 'ИЯ', res)
res = len(list(res))
print(res)