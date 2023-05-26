import itertools as it


alph = '01234'
res = it.product(alph, repeat=6)
res = filter(lambda x: ''.join(x), res)
res = filter(lambda x: x[-1] not in '34', res)
res = filter(lambda x: x[0] not in '01', res)
res = len(list(res))
print(res)
