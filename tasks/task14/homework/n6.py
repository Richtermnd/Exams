def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(1, 5000):
        a = 4 ** 2015 + 2 ** x - 2 ** 2015 + 15
        if bin(a)[2:].count('1') == 500:
            print(x)
            break


main()