from fnmatch import fnmatch


def divs(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def even_divs(n):
    return [x for x in divs(n) if x % 2 == 0]


def main():
    mask = '6*97*5?'
    i = 65_000
    cnt = 7
    while cnt:
        i += 1
        if fnmatch(str(i), mask): 
            d = even_divs(i)
            # print(i, d)
            if len(d) >= 4:
                print(i, sum(d))
                cnt -= 1


main()