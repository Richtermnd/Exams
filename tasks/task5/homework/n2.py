def f(n):
    r = bin(n)[2:]
    r += '10' if n % 2 else '01'
    return int(r, 2)


def solution():
    res = []
    for i in range(100):
        if f(i) > 81:
            res.append(f(i))
    print(min(res))

    
solution()