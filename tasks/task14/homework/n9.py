def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    a = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
    print(to_dec(a, 12).count(11))


main()