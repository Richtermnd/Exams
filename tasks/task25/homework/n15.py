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
    while cnt != 7:
        i -= 1
        divs = div(i)[1:-1]
        s = sum(x for x in divs if len(div(x)) == 2)
        if s and s % 10 == 0:
            cnt += 1
            print(i, s)

main()
