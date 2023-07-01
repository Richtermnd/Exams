def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    res = []
    for i in range(81_234, 134_689 + 1):
        divs = div(i)
        divs = divs[1:-1]
        if len(divs) == 3:
            res.append(divs)
    for x in res:
        print(*x)



main()
