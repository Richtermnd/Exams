from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if ((w <= y) or not (y <= z)) and not x and not (x == z):
        print(x, y, z, w)
