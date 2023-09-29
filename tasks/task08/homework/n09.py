import itertools as it

res = range(5 ** 5, 5 ** 6)
res = filter(lambda x: x % 5 != 3 and x % 5 != 4 and x // 5 ** 5 != 1, res)
res = len(list(res))
print(res)