import itertools as it


alph = 'САЛО'
res = it.product(alph, repeat=6)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: 0 < x.count('О') <= 3, res)
res = len(list(res))
print(res)