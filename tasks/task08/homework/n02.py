import itertools as it


alph = 'AAABBBB'
res = it.product(alph, repeat=6)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x == 'BAAAAB', res)
res = len(list(res))
print(res)