def f(n):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return f(n - 2) + n - 2
    return f(n + 2) + n + 2


def main():
    n = 1
    res = f(n)
    cnt = 0
    while res < 10_000:
        n += 1
        try:
            res = f(n)
        except:
            pass
    
    while res < 100_000:
        n += 1
        try:
            res = f(n)
            cnt += 1
        except:
            pass

    print(cnt)


main()