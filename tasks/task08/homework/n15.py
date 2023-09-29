import itertools as it


alph = 'БЕЙББББА'
res = it.permutations(alph, r=6)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: 'ЙБ' in x, res)
res = len(list(res))
print(res)