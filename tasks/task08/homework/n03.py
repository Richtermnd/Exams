import itertools as it


alph = 'ПУЛЯ'
res = it.product(alph, repeat=6)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x.count('У') == 2, res)
res = len(list(res))
print(res)