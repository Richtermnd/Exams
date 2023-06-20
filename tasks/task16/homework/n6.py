def f(n):
    if n <= 1:
        return 1
    if n % 2:
        return 2 * f(n - 2)
    return 3 * n + f(n - 1)


def main():
    print(f(31))


main()