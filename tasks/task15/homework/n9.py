from itertools import combinations, product


def sets():
    """ Решай аналитически и кодом """
    a = set()
    bits = set(''.join(elem) for elem in product('01', repeat=8))
    p = {elem for elem in bits if elem.startswith('11')}
    q = {elem for elem in bits if elem.endswith('0')}

    def f(x):
        A = x in a
        P = x in p
        Q = x in q

        return (not A) <= (P or not Q)

    for x in product('01', repeat=8):
        if not f(''.join(x)):
            a.add(x)
    
    print(len(a))


def segments():
    """ Решай аналитически и кодом """
    
    def f(x, a1, a2):
        A = a1 <= x <= a2
        D = ... <= x <= ...
        C = ... <= x <= ...
        return ...
    
    linespace = [x / 4 for x in range(... * 4, ... * 4 + 1)]

    res = ...
    for a1, a2 in combinations(linespace, 2):
        if all(f(x, a1, a2) for x in linespace):
            res = ...
    
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


sets()
