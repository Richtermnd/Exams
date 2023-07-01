def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    """ Трешатина """
    for i in range(55_000_000, 60_000_000 + 1):
        x = i
        while x % 2 == 0:
            x //= 2
        if int(x ** 0.25) ** 4 == x and len(div(int(x ** 0.25))) == 2:
            print(i, x)


main()
