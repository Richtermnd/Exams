from functools import lru_cache


@lru_cache(None)
def f(n):
    if n > 30:
        return n ** 2 + 5 * n + 4
    if n % 2 == 0:
        return f(n + 1) + 3 * f(n + 4)
    return 2 * f(n + 2) + f(n + 5)


def main():
    cnt = 0
    for n in range(1, 1_001):
        cnt += sum(int(x) for x in str(f(n))) == 27
    print(cnt)


main()