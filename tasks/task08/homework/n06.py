import itertools as it


alph = 'ИГРОК'
res = it.permutations(alph)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x[0] != 'К' and 'РОК' not in x, res)
res = len(list(res))
print(res)