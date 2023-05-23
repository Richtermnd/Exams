from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if ((not x and y) == z) and w:
        print(x, y, z, w)

print('x y z w')
z = 0
w = 1
for x, y in product([0, 1], repeat=2):
    if ((not x and y) == z) and w:
        print(x, y, z, w)