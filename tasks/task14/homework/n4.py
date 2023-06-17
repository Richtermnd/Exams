def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    a = 51 * 7 ** 12 - 7 ** 3 -22
    print(sum(to_dec(a, 7)))


main()