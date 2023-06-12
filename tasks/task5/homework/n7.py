def f(n):
    r = bin(n)[2:]
    r += str(sum(int(x) for x in r) % 2)
    r += str(sum(int(x) for x in r) % 2)
    return int(r, 2)


def solution():
    res = set()
    for i in range(50):
        if f(i) < 80:
            res.add(f(i))
        print(f(i))
    print(len(res))
solution()