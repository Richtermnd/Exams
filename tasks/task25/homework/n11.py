def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    cnt = 0
    i = 300_000
    while cnt != 4:
        i += 1
        divs = div(i)[:-1]
        if sum(x % 3 == 0 and x != i for x in divs) == 5:
            cnt += 1
            print(i, max(x for x in divs if x % 3 == 0 and x != i))


main()
