def f(n):
    if n <= 3:
        return 3
    if n % 2 == 0:
        return f(n // 2) + 5
    return f(n - 1) - f(n - 2)


def main():
    print(f(20))


main()