import itertools as it


alph = 'ВИШНЯ'
res = it.product(alph, repeat=6)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x.count('В') <= 1, res)
res = filter(lambda x: x[0] != 'Ш', res)
res = filter(lambda x: x[-1] not in 'ИЯ', res)
res = len(list(res))
print(res)