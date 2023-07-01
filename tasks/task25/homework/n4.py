def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    cnt = 0
    i = 150_000 + 1
    while cnt != 7:
        divs = div(i)[1:-1]
        if sum(divs) % 13 == 10:
            cnt += 1
            print(i, sum(divs))
        i += 1


main()
