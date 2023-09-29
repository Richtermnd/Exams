def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(15):
        a = 9 * 17 ** 4 + \
            7 * 17 ** 3 + \
            5 * 17 ** 2 + \
            9 * 17 ** 1 + \
            x * 17 ** 0
        
        b = 3 * 17 ** 4 + \
            x * 17 ** 3 + \
            1 * 17 ** 2 + \
            0 * 17 ** 1 + \
            8 * 17 ** 0
        
        if (a + b) % 11 == 0:
            print((a + b) // 11)


main()