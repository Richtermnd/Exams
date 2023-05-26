import itertools as it


alph = 'игрок'
res = it.permutations(alph)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x[0] != 'к', res)
res = filter(lambda x: 'рок' not in x, res)
res = len(list(res))


print(res)
