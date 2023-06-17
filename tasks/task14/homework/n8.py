def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(1, 5000):
        a = 36 ** 17 - 6 ** x + 71
        if sum(to_dec(a, 6)) == 61:
            print(x)
            break


main()