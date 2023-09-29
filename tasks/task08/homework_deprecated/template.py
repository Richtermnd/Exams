import itertools as it


alph = ''
res = it.product(alph, repeat=6)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x, res)
res = len(list(res))
print(res)