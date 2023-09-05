import itertools as it


alph = 'мария'
cnt = 0
for i, word in enumerate(sorted(list(it.product(alph, repeat=4)))):
    word = ''.join(word)
    if word == 'ария':
        cnt = i + 1

print(cnt)
