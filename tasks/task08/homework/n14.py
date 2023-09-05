import itertools as it


alph = 'дейкстра'
res = it.permutations(alph, r=6)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x.count('й') == 1, res)
res = filter(lambda x: x.find('й') != 5, res)
res = filter(lambda x: x[x.find('й') + 1] in 'дкстр', res)
res = len(list(res))
print(res)