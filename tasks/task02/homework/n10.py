from itertools import product


print('x y z f')
for x, y, z in product([0, 1], repeat=3):
    print(x, y, z, int(not (x == (y <= z))))