def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    for i in range(25_317, 51_237 + 1):
        divs = div(i)[:-1]
        if sum(len(div(x)) == 2 for x in divs) >= 6:
            print(i, max(x for x in divs if len(div(x)) == 2))


main()
