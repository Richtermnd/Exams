import itertools as it


alph = 'лемур'
res = set(it.permutations(alph))
res = map(lambda x: ''.join(x), res)
res = len(list(res))
print(res)