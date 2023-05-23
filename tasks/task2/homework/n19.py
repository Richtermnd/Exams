from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if ((x and z) or ((w <= x) == (z <= y))) == 0:
        print(x, y, z, w)
