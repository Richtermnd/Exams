def tern(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]
        

def f(n):
    r = tern(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += tern(n % 3 * 5)
    return int(r, 3)


res = float('inf')

for i in range(1, 1000):
    a = f(i)
    if a > 133:
        res = min(res, a)
print(res)