import itertools as it


alph = 'ABCWXYZ'
cnt = 0
for word in it.product('WXYZ', *['ABC'] * 4, 'WXYZ'):
    # word = ''.join(word)
    cnt += 1

print(cnt)
