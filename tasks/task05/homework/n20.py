from math import prod


def f(n, m):
    nm = str(n) + str(m)
    p1 = prod(int(x) for x in nm if x != '0' and int(x) % 2 == 0)
    p2 = prod(int(x) for x in nm if int(x) % 2)
    return abs(p1 - p2)

def solution():
    for i in range(1, 10000):
        if f(i, 120) == 29:
            print(i)
            break

    
solution()