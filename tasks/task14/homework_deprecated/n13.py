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
n^2 + 3n + 2 + 11 = (n + 1)^2 + 2n + 2 + 4
n^2 + 3n + 2 + 11 = n^2 + 2n + 1 + 2n + 2 + 4
n = 6
"""