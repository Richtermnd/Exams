def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(1, 5000):
        a = 4 ** 1014 - 2 ** x + 12
        if bin(a)[2:].count('0') == 2000:
            print(x)
            break


main()