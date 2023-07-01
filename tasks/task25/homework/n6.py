def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    cnt = 0
    i = 550_000 + 1
    while cnt != 5:
        divs = div(i)[1:-1]
        f = int(sum(divs) / len(divs)) if len(divs) > 0 else 0
        if f % 31 == 13:
            cnt += 1
            print(i, f)
        i += 1
        




main()
