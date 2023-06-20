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
        A = div(x, a) and div(x, 24) and not div(x, 16)
        B = not div(x, a)
        return A <= B

    for a in range(1, 10000):
        if all(f(x, a) for x in range(1, 100000)):
            print(a)
            break    
    


def numbers():
    
    def f(x, a):
        A = ...
        B = ...
        return ...
    
    for a in range(1, 10_000):
        if all(f(x, a) for x in range(1, 100_000)):
            print(a)


divs()
