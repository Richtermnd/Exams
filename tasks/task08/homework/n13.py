import itertools as it


alph = '0123456789'
res = it.product(alph, repeat=3)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x[0] != '0', res)
res = filter(lambda x: list(x) == sorted(x), res)
res = len(list(res))
print(res)