def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(1, 1000):
        a = 125 ** 200 - 5 ** x + 74
        if to_dec(a, 5).count(4) == 100:
            print(x)
            break


main()