from itertools import product


print('a b c d')
for a, b, c, d in product([0, 1], repeat=4):
    if ((not a and not b) or (b == c) or d) == 0:
        print(a, b, c, d)
