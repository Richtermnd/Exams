from itertools import combinations


def sets():
    """ Решай аналитически и кодом """
    a = set()
    b = {...}
    c = {...}

    def f(x):
        A = x in a
        B = x in b
        C = x in c
        return ...

    for x in range(1, 100_000):
        if not f(x):
            a.add(x)
    
    print(a)


def segments():
    """ Решай аналитически и кодом """
    
    def f(x, a1, a2):
        A = a1 <= x <= a2
        B = 18 <= x <= 52
        C = 16 <= x <= 41
        return (B <= A) and (not C or A)
    
    linespace = [x / 4 for x in range(16 * 4, 52 * 4 + 1)]

    res = float('inf')
    for a1, a2 in combinations(linespace, 2):
        if all(f(x, a1, a2) for x in linespace):
            res = min(res, a2 - a1)
    
    print(round(res))


def divs():
    
    def div(n, m):
        return n % m == 0
    
    def f(x, a):
        A = ...
        B = ...
        return ...
    
    for a in range(1, 10_000):
        if all(f(x, a) for x in range(1, 100_000)):
            print(a)


def numbers():
    
    def f(x, a):
        A = ...
        B = ...
        return ...
    
    for a in range(1, 10_000):
        if all(f(x, a) for x in range(1, 100_000)):
            print(a)


segments()
