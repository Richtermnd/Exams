import itertools as it


alph = 'вайфу'
res = it.permutations(alph, r=4)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x[0] != 'й', res)
res = filter(lambda x: 'вф' not in x, res)
res = filter(lambda x: 'фв' not in x, res)
res = len(list(res))
print(res)