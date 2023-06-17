def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(15):
        a = 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
        b = 15 ** 4 + x * 15 ** 3 + 2 * 15 ** 2 + 3 * 15 + 3
        if (a + b) % 14 == 0:
            print(x, (a + b) // 14)


main()