def f(n):
    if n <= 10:
        return n
    if n <= 36:
        return n // 4 + f(n - 10)
    return 2 * f( n - 5)


def main():
    print(f(100))


main()