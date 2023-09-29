import itertools as it


alph = 'ЛОДКА'
res = it.product(alph, repeat=4)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x.count('О') >= 2, res)
res = len(list(res))
print(res)