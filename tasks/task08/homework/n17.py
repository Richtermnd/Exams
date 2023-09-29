import itertools as it


alph = 'МИМИКРИЯ'
res = it.permutations(alph)
res = len(set(res))  # set убирает повторы
print(res)