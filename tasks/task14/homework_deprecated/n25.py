def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(21):
        for y in range(21):
            a = 1 * 21 ** 4 + 2 * 21 ** 3 + y * 21 ** 2 + x * 21 + 9
            b = 3 * 21 ** 4 + 6 * 21 ** 3 + y * 21 ** 2 + 9 * 21 + 9
            if (a + b) % 18 == 0:
                y = 5
                a = 1 * 21 ** 4 + 2 * 21 ** 3 + y * 21 ** 2 + x * 21 + 9
                b = 3 * 21 ** 4 + 6 * 21 ** 3 + y * 21 ** 2 + 9 * 21 + 9
                print((a + b) // 18)
                return



main()