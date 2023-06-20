from functools import lru_cache


@lru_cache
def f(n):
    if n > 10_000:
        return n - 10_000
    return f(n + 1) + f(n + 2)

def main():
    for i in range(10_001, 0, -1):
        f(i)
    
    print(f(12_345) * (f(10) - f(12)) / f(11) + f(10_101))


main()