def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    a = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
    res = to_dec(a, 6)
    print(res.count(5) - res.count(0))


main()