import itertools as it


res = 0
for x in range(100, 1000):
    digits = [int(x) for x in str(x)]
    if digits == sorted(digits):
        res += 1
print(res)