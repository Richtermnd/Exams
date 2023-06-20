from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 18:
        return n + 3
    if n % 3 == 0:
        return (n // 3) * f(n // 3) + n - 12 
    return f(n - 1) + n ** 2 + 5


def main():
    cnt = 0
    for n in range(1, 1_001):
        cnt += all(int(x) % 2 == 0 for x in str(f(n)))
    print(cnt)


main()