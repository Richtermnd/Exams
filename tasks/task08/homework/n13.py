import itertools as it


alph = 'гепард'
res = it.product(alph, repeat=5)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x.count('г') == 1 and x[0] != 'а' and x[-1] != 'е', res)
res = len(list(res))
print(res)