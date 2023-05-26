import itertools as it


alph = 'лодка'
cnt = 0
for word in it.product(alph, repeat=4):
    word = ''.join(word)
    if word.count('о') >= 2:
        cnt += 1

print(cnt)
