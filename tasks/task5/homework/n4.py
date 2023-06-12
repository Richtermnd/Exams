def f(n):
    r = bin(n)[2:]
    r += r[-1]
    r += '1' if r.count('1') % 2 else '0'
    r += '1' if r.count('1') % 2 else '0'
    return int(r, 2)


def solution():
    res = []
    for i in range(100):
        if f(i) > 144:
            res.append(f(i))
    print(min(res))
    

solution()