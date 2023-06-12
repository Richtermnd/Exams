def f(n):
    r = bin(n)[2:]
    r = r[::-1]
    return int(r, 2)


def solution():
    res = []
    for i in range(1, 100):
        if f(i) == 13:
            res.append(i)
    print(max(res))

    
solution()