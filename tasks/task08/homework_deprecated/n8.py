import itertools as it


alph = 'ab123'
cnt = 0
for word in it.product(alph, repeat=...):
    word = ''.join(word)
    if ...:
        cnt += 1

print(cnt)
