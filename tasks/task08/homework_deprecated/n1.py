import itertools as it


alph = 'КРЕСЛО'
cnt = 0
for word in it.product(alph, repeat=4):
    word = ''.join(word)
    if word[0] in 'КРСЛ' and word[-1] in 'ЕО':
        cnt += 1

print(cnt)
