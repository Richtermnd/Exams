def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    x = 3 * 16 ** 8 - 4 ** 5 + 3
    print(to_n(x, 4).count(3))

main()