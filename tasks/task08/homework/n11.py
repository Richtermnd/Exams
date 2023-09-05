import itertools as it

alph = 'abcd'
res = it.product(alph, repeat=4)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x == ''.join(sorted(x)), res)
res = len(list(res))
print(res)