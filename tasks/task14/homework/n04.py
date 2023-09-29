def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    x = 51 * 7 ** 12 - 7 ** 3 - 22
    print(sum(to_n(x, 7)))

main()