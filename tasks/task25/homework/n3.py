def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    for i in range(154_026, 154_043 + 1):
        divs = div(i)
        if len(divs) == 4:
            print(*divs[-2:])



main()
