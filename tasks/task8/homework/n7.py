import itertools as it


alph = 'абиколун'
res = it.permutations(alph)
res = map(lambda x: ''.join(x), res)

vowel = 'аиоу'
vowel_pairs = it.product(vowel, repeat=2)
vowel_pairs = list(map(lambda x: ''.join(x), vowel_pairs))

consonant = 'бклн'
consonant_pairs = it.product(consonant, repeat=2)
consonant_pairs = list(map(lambda x: ''.join(x), consonant_pairs))

vowel_valid = lambda word: all(map(lambda x: x not in word, vowel_pairs))
consonant_valid = lambda word: all(map(lambda x: x not in word, consonant_pairs))

res = filter(vowel_valid, res)
res = filter(consonant_valid, res)

res = len(list(res))

print(res)
