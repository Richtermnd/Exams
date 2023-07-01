def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    for i in range(1_204_300, 1_204_380 + 1):
        divs = div(i)
        s = sum(x for x in divs[:-1] if x % 2 == 0)
        if s and s % 10 == 0:
            print(i, s)


main()
