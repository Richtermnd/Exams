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
n ^ 2 + 3 = 9(n + 2) + 7
n ^ 2 - 9n - 22 = 0
"""