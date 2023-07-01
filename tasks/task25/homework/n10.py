def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    cnt = 0
    i = 500_000
    while cnt != 5:
        i += 1
        divs = div(i)[:-1]
        if any(x % 10 == 8 and x != 8 for x in divs):
            cnt += 1
            print(i, min(x for x in divs if x % 10 == 8 and x != 8))
        


main()
