def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    for i in range(113_000_000, 114_000_001):
        if i % 2 == 0 and i % 4 != 0:
            x = i // 2
            if int(x ** 0.5) ** 2 == x and len(div(int(x ** 0.5))) == 2:
                print(i, 2 * int(x ** 0.5))



main()
