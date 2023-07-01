from math import prod


def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    cnt = 0
    i = 400_000_000

    while cnt != 5:
        i += 1
        divs = div(i)[1:-1]
        p = prod(divs[:5]) if len(divs) >= 5 else 0

        if p % 100 == 17 and p <= i:
            cnt += 1
            print(p, max(divs[:5]))


main()
