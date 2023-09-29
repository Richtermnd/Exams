def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(40):
        if to_n(x, 2)[-4:] == [1, 0, 1, 1]:
            print(x)


main()