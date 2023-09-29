def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(11):
        a = 3 * 11 ** 4 + 3 * 11 ** 3 + 6 * 11 ** 2 + 4 * 11 + x
        b = x * 12 ** 4 + 7 * 12 ** 3 + 9 * 12 ** 2 + 4 * 12 + 6
        c = 5 * 14 ** 4 + 5 * 14 ** 3 + x * 14 ** 2 + 8 * 14 + 7
        if a + b == c:
            print(c)
            break

main()