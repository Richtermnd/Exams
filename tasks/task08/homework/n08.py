import itertools as it


alph = 'AA111'
res = it.product(alph, repeat=8)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x.count('A') == 2, res)
res = len(list(res))
print(res)