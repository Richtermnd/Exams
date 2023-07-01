def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    cnt = 0
    i = 250_200
    while cnt != 5:
        i += 1
        divs = div(i)[1:-1]
        
        if len(divs) <= 1:
            continue

        if (divs[-1] + divs[0]) % 123 == 17:
            cnt += 1
            print(i, divs[-1] + divs[0])


main()
