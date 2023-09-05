import itertools as it


alph = 'лемур'
cnt = 0
for word in sorted(list(it.product(alph, repeat=4))):
    cnt += 1
    word = ''.join(word)
    if word[0] == 'л':
        print(cnt)
        break

print(cnt)
