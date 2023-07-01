def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    res = []
    for i in range(174_457, 174_505 + 1):
        divs = div(i)
        divs = divs[1:-1]
        if len(divs) == 2:
            res.append(divs)
    
    res.sort(key=lambda x: x[0] * x[1])
    for pair in res:
        print(*pair)


main()
