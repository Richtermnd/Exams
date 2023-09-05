def f(n):
    r = bin(2 * n)[2:]
    r += str(sum(int(x) for x in r) % 2)
    r += str(sum(int(x) for x in r) % 2)
    return int(r, 2)


def solution():
    i = 1
    while f(i) <= 1017:
        i += 1

    print(i)

    
solution()