def tern(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]
        

def f(n):
    r = tern(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += tern(n % 3 * 4)
    return int(r, 3)


res = 0

for i in range(1, 1000):
    a = f(i)
    if a < 191:
        res = max(res, i)
print(res)