def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    x = 64 ** 30 + 2 ** 300 - 4
    print(to_n(x, 8).count(7))


main()