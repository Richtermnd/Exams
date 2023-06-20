def f(n):
    cnt = 1
    if n >= 1:
        cnt += 2 + f(n - 1) + f( n -3)
    return cnt


def main():
    print(f(40))


main()