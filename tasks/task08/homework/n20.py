import itertools as it


alph = 'МАРИЯ'
words = it.product(alph, repeat=4)
res = 0
for i, word in enumerate(sorted(words)):
    if word == tuple('АРИЯ'):
        res = i + 1
print(res)