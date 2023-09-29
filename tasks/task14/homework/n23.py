def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(15):
        a = 1 * 15 ** 4 + \
            2 * 15 ** 3 + \
            3 * 15 ** 2 + \
            x * 15 ** 1 + \
            5 * 15 ** 0
        
        for y in range(17):
            b = 6 * 17 ** 3 + \
                7 * 17 ** 2 + \
                y * 17 ** 1 + \
                9 * 17 ** 0
            c = a + b
            if c % 131 == 0:
                print(x, y, c // 131)


main()