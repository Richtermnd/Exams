from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if (((z <= x) and x <= w) or (y == (z or x))) == 0:
        print(x, y, z, w)
