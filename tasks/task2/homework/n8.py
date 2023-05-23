from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if not y and x and (not z or w):
        print(x, y, z, w)
from itertools import product


print('x y z w')
for x, y, z in product([0, 1], repeat=3):
    if (y <= (x or z) and (z <= y)) == 0:
        print(x, y, z)
