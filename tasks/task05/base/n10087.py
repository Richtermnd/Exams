def f(n):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin(n % 3 * 3)[2:]
    return int(r, 2)

res = float('inf')

for i in range(1, 1000):
    a = f(i)
    if a > 151:
        res = min(res, a)
print(res)