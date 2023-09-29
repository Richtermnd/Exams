def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    a = 2 * 27 ** 7 + 3 ** 10 - 9
    print(to_dec(a, 3).count(0))


main()