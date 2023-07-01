def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    for i in range(190_201, 190_260 + 1):
        divs = div(i)
        divs = [x for x in divs if x % 2 == 0]
        if len(divs) == 4:
            print(*divs[-1:-3:-1])


main()
