from itertools import product


print('a b c')
for a, b, c in product([0, 1], repeat=3):
    if (a and b) or (not b and not c):
        print(a, b, c)