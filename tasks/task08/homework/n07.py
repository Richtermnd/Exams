import itertools as it


alph = 'АБАБАБАБ'
res = it.permutations(alph)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: 'ББ' not in x and 'АА' not in x, res)
res = len(list(res))
print(res)