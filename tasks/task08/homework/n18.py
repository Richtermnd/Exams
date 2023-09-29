import itertools as it


alph = 'ЛЕМУР'
words = it.product(alph, repeat=4)
words = sorted(words)
res = 0
for _ in it.takewhile(lambda x: x[0] != 'Л', words):
    res += 1
print(res + 1)