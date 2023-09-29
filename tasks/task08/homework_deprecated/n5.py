import itertools as it


alph = 'САЛО'
cnt = 0
for word in it.product(alph, repeat=6):
    word = ''.join(word)
    if 1 <= word.count('О') <= 3:
        cnt += 1

print(cnt)
