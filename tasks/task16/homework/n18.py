def f(n):
    cnt = n * n
    if n > 1:
        cnt += 2 * n + 1 + f(n - 2) + f(n // 3)
    return cnt


def main():
    print(f(100))


main()