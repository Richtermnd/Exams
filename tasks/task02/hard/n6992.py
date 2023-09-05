import itertools as it


print('x y z w')
for x, y, z, w in set(it.permutations((1, 1, 0, 0))):
    if (w <= y) == (x and z):
        print(x, y, z, w)
print()

print('x y z w')
for x, y, z, w in set(it.permutations((0, 1, 1, 1))):
    if (not x or not y or not z or w) == 0:
        print(x, y, z, w)
print()


print('x y z w')
for x, y, z, w in set(it.permutations((1, 1, 1, 0))):
    if (z or w) and y and x:
        print(x, y, z, w)


# ответ wxyz