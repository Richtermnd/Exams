import itertools as it


alph = 'ABCD'
res = it.product(alph, repeat=4)
# res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x == tuple(sorted(x)), res)  # Нельзя сравнивать с генератором.
res = len(list(res))
print(res)