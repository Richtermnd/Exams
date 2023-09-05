from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if (not (z and not w) or ((z <= w) == (x <= y))) == 0:
        print(x, y, z, w)
