def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    x = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
    print(to_n(x, 12).count(11))


main()