def f(n):
    r = bin(n)[2:]
    if sum(int(x) for x in r) % 2:
        r += '1'
        r = '11' + r[2:]
    else:
        r += '0'
        r = '10' + r[2:]

    return int(r, 2)


def solution():
    res = []
    for i in range(1, 100):
        if f(i) < 35:
            res.append(i)
    print(max(res))

    
solution()