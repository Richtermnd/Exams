def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    a = 3 * 16 ** 8 - 4 ** 5 + 3
    print(to_dec(a, 4).count(3))


main()