def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    a = 64 ** 30 + 2 ** 300 - 4
    print(to_dec(a, 8).count(7))


main()