def f(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + f( n / 3)
    return n + f(n + 3)


def main():
    n = 1
    res = f(n)
    while res <= 100:
        n += 1
        try:
            res = f(n)
        except:
            pass
    print(n)


main()