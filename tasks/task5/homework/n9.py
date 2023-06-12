def f(n):
    r = bin(n)[2:]
    if n % 2:
        r = '11' + r + '11'
    else:
        r = '1' + r + '0'

    return int(r, 2)


def solution():
    res = []
    for i in range(1000):
        if f(i) > 52:
            res.append(f(i))
    print(min(res))


solution()