def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(8, 100):
        if int('103', x) == int('97', x + 2):
            print(x)
            break


main()