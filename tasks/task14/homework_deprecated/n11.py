def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    pass


main()


"""
(3 * (x + 4) + 3) - (3 * 4 + 3) = 33
3 * (x + 4) + 3 - 12 - 3 = 33
3 * (x + 4) = 33 - 3 + 12 + 3
x = 11
"""