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
        
        b = 1 * 15 ** 4 + \
            x * 15 ** 3 + \
            2 * 15 ** 2 + \
            3 * 15 ** 1 + \
            3 * 15 ** 0
        
        if (a + b) % 14 == 0:
            print((a + b) // 14)

main()