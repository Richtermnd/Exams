import itertools as it


alph = 'мария'
res = list(it.product(alph, repeat=4))
res.sort()
print(res[210])
