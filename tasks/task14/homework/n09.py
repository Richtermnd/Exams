def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for a in range(1000):
        x = 36 ** 17 - 6 ** a + 71
        if sum(to_n(x, 6)) == 61:
            print(a)
            break


main()