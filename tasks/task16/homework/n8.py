def f(n):
    if n <= 2:
        return n
    if n % 2 == 0:
        return int((n + f(n - 2)) / 5)
    return int((2 * n + f(n - 1) + f(n - 2)) / 4)


def main():
    print(f(50))


main()