import itertools as it


alph = 'пуля'
cnt = 0
for word in it.product(alph, repeat=6):
    word = ''.join(word)
    if word.count('у') == 2:
        cnt += 1

print(cnt)
