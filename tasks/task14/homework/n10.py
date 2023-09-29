def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    x = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
    h = to_n(x, 6)
    print(h.count(5) - h.count(0))


main()