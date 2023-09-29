def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    x = 2 * 27 ** 7 + 3 ** 10 - 9
    print(to_n(x, 3).count(0))


main()
