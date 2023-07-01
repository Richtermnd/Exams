def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    """  """
    print(2 ** 4 * 3 ** 4 * 5 ** 4 * 7 * 11 * 13, 13)


main()

