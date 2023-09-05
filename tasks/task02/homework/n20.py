from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if ((x == (not z)) <= ((x or w) == y)) == 0 and not y:
        print(x, y, z, w)
