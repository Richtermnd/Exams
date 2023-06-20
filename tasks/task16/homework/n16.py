from functools import lru_cache


@lru_cache
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return f(n // 2) + 1
    return f(n - 1) + n


def main():
    n = 1
    while f(n) != 19:
        n += 1
    print(n)

main()