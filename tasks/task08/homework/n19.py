import itertools as it


alph = 'АЛГОРИТМ'
words = it.product(alph, repeat=4)
words = sorted(words)
res = 0
for i, word in enumerate(words):
    if word[-2:] == ('И', 'М'):
        res = i + 1

print(res)


