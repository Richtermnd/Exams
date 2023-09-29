import itertools as it


alph = 'МАРИЯ'
res = it.product(alph, repeat=4)
for i, word in enumerate(sorted(res)):
    if i == 210:
        print(word)
        break