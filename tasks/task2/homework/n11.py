from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if ((y <= x) or not ((x <= z) and (z <= x)) and not w) == 0:
        print(x, y, z, w)
