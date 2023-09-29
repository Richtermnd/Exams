import itertools as it


alph = 'КРЕСЛО'
res = it.product(alph, repeat=4)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x[0] in 'КРСЛ' and x[-1] in 'ЕО', res)
res = len(list(res))
print(res)