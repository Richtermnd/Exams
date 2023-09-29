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
(2x + 1) * (x + 3) = 3x^2 + x + 3
2x^2 + 6x + x + 3 = 3x^2 + x + 3
x^2 - 6x = 0
x = 6
"""